//다중 집합으로 변경하기
const multiple = (content, check_eng) => {
  const multipleSet = [];
  for (let i = 0; i < content.length - 1; i++) {
    if (check_eng.test(content[i]) && check_eng.test(content[i + 1]))
      multipleSet.push(content[i] + content[i + 1]);
  }
  return multipleSet;
};

function solution(str1, str2) {
  let answer = 0;
  const plusSet = [];
  const dupSet = [];
  const check_eng = /[A-Z]/;
  const set1 = multiple(str1.toUpperCase(), check_eng);
  const set2 = multiple(str2.toUpperCase(), check_eng);

  set1.forEach((item) => {
    if (set2.includes(item)) {
      dupSet.push(item);
      plusSet.push(item);
      set2.splice(set2.indexOf(item), 1);
    } else plusSet.push(item);
  });

  set2.forEach((item) => {
    if (set1.includes(item)) {
      plusSet.push(item);
    } else plusSet.push(item);
  });
  // 0나누기0 예외처리
  answer =
    dupSet.length === 0 && plusSet.length === 0
      ? 65536
      : parseInt((dupSet.length / plusSet.length) * 65536);

  return answer;
}
