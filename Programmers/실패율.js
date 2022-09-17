function solution(N, stages) {
  let stageUser = stages.length;
  let answer = [];

  for (let i = 1; i <= N + 1; i++) {
    let tmp = stages.filter((num) => num === i).length;
    answer.push([i, tmp / stageUser]);
    stageUser -= tmp;
  }

  answer.pop();
  answer = answer.sort((a, b) => b[1] - a[1]);

  return answer.map((ans) => ans[0]);
}
