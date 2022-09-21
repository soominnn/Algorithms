const multiple = (content) => {
  let multipleSet = [];
  for (let i = 0; i < content.length - 1; i++) {
    multipleSet.push(content[i] + content[i + 1]);
  }
  return multipleSet;
};

function solution(str1, str2) {
  let answer = 0;
  let plusSet = [];
  let dupSet = [];
  let check_eng = /[A-Z]/;
  let set1 = multiple(str1.toUpperCase());
  let set2 = multiple(str2.toUpperCase());
  set1.forEach((item) => {
    if (check_eng.test(item) && set2.includes(item)) {
      dupSet.push(item);
    } else plusSet.push(item);
  });
  set2.forEach((item) => {
    if (check_eng.test(item) && set1.includes(item)) {
      dupSet.push(item);
    } else plusSet.push(item);
  });

  return answer;
}
