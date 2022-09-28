function solution(numbers) {
  let answer = numbers.map((num) => num + "").sort((a, b) => b + a - (a + b));
  return answer.every((a) => a === "0") ? "0" : answer.join("");
}
