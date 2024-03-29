const repet = (answers, arr, result) => {
  let index = 0;
  let cnt = 0;
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === arr[index]) cnt += 1;
    index++;
    if (index === arr.length) index = 0;
  }
  result.push(cnt);
  return result;
};

function solution(answers) {
  let one = [1, 2, 3, 4, 5];
  let two = [2, 1, 2, 3, 2, 4, 2, 5];
  let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let result = [];
  let answer = [];

  result = repet(
    answers,
    three,
    repet(answers, two, repet(answers, one, result))
  );

  let maxValue = Math.max(...result);
  for (let i = 0; i < result.length; i++)
    if (maxValue === result[i]) answer.push(i + 1);

  return answer;
}
