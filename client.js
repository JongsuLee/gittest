const { io } = require("socket.io-client");

// 서버 URL을 입력하세요 (예: http://localhost:3000)
const SERVER_URL = "http://localhost:8000";

console.log(`${SERVER_URL}/vibe/session`);
const socket = io(`${SERVER_URL}/vibe/session`, {
  reconnectionAttempts: 5,
  timeout: 10000,
  transports: ["websocket", "polling"], // websocket 먼저 시도
});

session_id = "123";
current_branch = "main";
path = "";

// 연결 성공 시
socket.on("connect", () => {
  console.log(`서버에 연결되었습니다. ID: ${socket.id}`);

  // 서버로 메시지 보내기 (이벤트명: "message")
  socket.emit("message", "안녕하세요, 서버!");
});

// 서버로부터 메시지 수신 시 (이벤트명: "response")
socket.on("whoami", (data) => {
  console.log("서버로부터 받은 데이터:", data);
  socket.emit("whoami", {
    session_id: session_id,
    current_branch: current_branch,
    path: path,
  });
});

// 서버로부터 메시지 수신 시 (이벤트명: "response")
socket.on("check_session", (data) => {
  console.log("서버로부터 받은 데이터:", data);
});

// 서버로부터 메시지 수신 시 (이벤트명: "response")
socket.on("response", (data) => {
  console.log("서버로부터 받은 데이터:", data);
});

// 연결 해제 시
socket.on("disconnect", (reason) => {
  console.log("서버와 연결이 끊어졌습니다. 사유:", reason);
});

// 연결 오류 발생 시
socket.on("connect_error", (error) => {
  console.error("연결 오류 발생:", error.message);
  if (error.message === "xhr poll error") {
    console.error(
      "→ 가능한 원인: 1) 서버가 실행 중인지 확인 (예: 포트 5000) 2) 서버 URL/경로가 맞는지 확인 3) CORS 설정 확인",
    );
  }
});
