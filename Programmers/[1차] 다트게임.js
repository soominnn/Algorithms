function solution(dartResult) {
  let answer = [];
  let calc = 0;

  for (let item of dartResult) {
    if (item === "*") {
      if (answer.length >= 2) {
        let temp1 = answer.at(-1) * 2;
        let temp2 = answer.at(-2) * 2;
        answer.pop();
        answer.pop();
        answer.push(temp2);
        answer.push(temp1);
      } else {
        let temp1 = answer.at(-1) * 2;
        answer.pop();
        answer.push(temp1);
      }
    } else if (item === "#") {
      let temp = answer.at(-1) * -1;
      answer.pop();
      answer.push(temp);
    } else if (item === "S") {
      calc = calc ** 1;
      answer.push(calc);
      calc = 0;
    } else if (item === "D") {
      calc = calc ** 2;
      answer.push(calc);
      calc = 0;
    } else if (item === "T") {
      calc = calc ** 3;
      answer.push(calc);
      calc = 0;
    } else calc += item;
  }

  let result;
  result = answer.reduce((a, b) => a + b);
  return result;
}
