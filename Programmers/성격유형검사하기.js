function solution(survey, choices) {
  let table = new Map();
  let answer = "";
  Array("R", "T", "C", "F", "J", "M", "A", "N").forEach((e) => table.set(e, 0));
  survey.forEach((e, i) => {
    if (choices[i] > 4)
      table.set(e[1], table.get(e[1]) + Math.abs(4 - choices[i]));
    else if (choices[i] < 4)
      table.set(e[0], table.get(e[0]) + Math.abs(4 - choices[i]));
  });
  Array("RT", "CF", "JM", "AN").forEach((e) => {
    answer += [...e].sort((a, b) => table.get(b) - table.get(a))[0];
  });
  return answer;
}
