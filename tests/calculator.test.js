const { add, subtract, multiply, divide } = require('../src/calculator');


describe('계산기 함수 테스트', () => {
  test('덧셈 함수가 올바르게 동작해야 한다', () => {
    expect(add(1, 2)).toBe(3);
    expect(add(-1, 1)).toBe(0);
    expect(add(-1, -1)).toBe(-2);
    expect(add(0.1, 0.2)).toBeCloseTo(0.3);
  });

  test('뺄셈 함수가 올바르게 동작해야 한다', () => {
    expect(subtract(5, 3)).toBe(2);
    expect(subtract(-1, 1)).toBe(-2);
    expect(subtract(0, 0)).toBe(0);
  });

  test('곱셈 함수가 올바르게 동작해야 한다', () => {
    expect(multiply(3, 4)).toBe(12);
    expect(multiply(-2, 3)).toBe(-6);
    expect(multiply(0, 5)).toBe(0);
  });

  test('나눗셈 함수가 올바르게 동작해야 한다', () => {
    expect(divide(10, 2)).toBe(5);
    expect(divide(-10, 2)).toBe(-5);
    expect(divide(7, 2)).toBe(3.5);
    
    expect(() => divide(10, 0)).toThrow('나눗셈은 0으로 나눌 수 없습니다.');
  });
});
