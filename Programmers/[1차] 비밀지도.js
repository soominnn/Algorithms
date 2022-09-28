//2진수 변경 함수
const transTo2 = (cnt, arr, n) => {
  arr.forEach((item, index) => {
    let remain = 0;
    for (let i = 0; i < n; i++) {
      remain = item % 2;
      item = parseInt(item / 2);
      cnt[index][n - i - 1] = remain;
    }
  });
  return cnt;
};

function solution(n, arr1, arr2) {
  let answer = new Array(n);
  answer.fill("");

  //두 배열의 행마다 각 칸의 2진수 변경값을 더하기 위한 배열 선언
  let res = new Array(n);
  for (let i = 0; i < n; i++) {
    res[i] = new Array(n);
  }

  //첫번째 배열을 위한 배열 선언
  let cnt1 = new Array(n);
  for (let i = 0; i < n; i++) {
    cnt1[i] = new Array(n);
  }

  //두번째 배열을 위한 배열 선언
  let cnt2 = new Array(n);
  for (let i = 0; i < n; i++) {
    cnt2[i] = new Array(n);
  }

  transTo2(cnt1, arr1, n); //첫번째 배열 2진수로 바꾸기
  transTo2(cnt2, arr2, n); //두번째 배열 2진수로 바꾸기

  //행마다 각 칸의 두 배열 2진수값들 더하기
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      res[i][j] = cnt1[i][j] + cnt2[i][j];
    }
  }

  //행마다 각 칸의 더한 값이 0보다 크면 #, 0이면 공백 추가하기
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (res[i][j] > 0) {
        answer[i] += "#";
      } else answer[i] += " ";
    }
  }

  return answer;
}
