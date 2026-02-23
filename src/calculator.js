
// 사칙연산 함수를 포함하는 계산기 모듈

// 덧셈 함수
function add(a, b) {
  return a + b;
}

// 뺄셈 함수
function subtract(a, b) {
  return a - b;
}


// 나눗셈 함수
function divide(a, b) {
  if (b === 0) {
    throw new Error("나눗셈은 0으로 나눌 수 없습니다.");
  }
  return a / b;
}

module.exports = {
  add,
  subtract,
  multiply,
  divide,
};


// 곱셈 함수
function multiply(a, b) {
  return a * b;
}

// 나눗셈 함수
function divide(a, b) {
  if (b === 0) {
    throw new Error("나눗셈은 0으로 나눌 수 없습니다.");
  }
  return a / b;
}

module.exports = {
  add,
  subtract,
  multiply,
  divide,
};