function solution(arr) {
  let answer = [];

  arr.map((num) => {
    if (answer[answer.length - 1] !== num) answer.push(num);
  });

  return answer;
}
