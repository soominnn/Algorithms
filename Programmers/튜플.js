function solution(s) {
  let answer = [];

  //문자열 나누고 요소들 길이에 따른 오름차순 정렬
  s = s
    .slice(2, -2)
    .split("},{")
    .sort((a, b) => {
      if (a.length > b.length) return 1;
      if (a.length < b.length) return -1;
    });

  //쉼표로 한번 더 나누고 answer에 없는 것들만 추출해서 answer에 넣기
  for (let item of s) {
    item = item.split(",");
    for (let i = 0; i < item.length; i++) {
      if (answer.includes(parseInt(item[i])) === false)
        answer.push(parseInt(item[i]));
    }
  }

  return answer;
}
