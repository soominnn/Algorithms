//2���� ���� �Լ�
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

  //�� �迭�� �ึ�� �� ĭ�� 2���� ���氪�� ���ϱ� ���� �迭 ����
  let res = new Array(n);
  for (let i = 0; i < n; i++) {
    res[i] = new Array(n);
  }

  //ù��° �迭�� ���� �迭 ����
  let cnt1 = new Array(n);
  for (let i = 0; i < n; i++) {
    cnt1[i] = new Array(n);
  }

  //�ι�° �迭�� ���� �迭 ����
  let cnt2 = new Array(n);
  for (let i = 0; i < n; i++) {
    cnt2[i] = new Array(n);
  }

  transTo2(cnt1, arr1, n); //ù��° �迭 2������ �ٲٱ�
  transTo2(cnt2, arr2, n); //�ι�° �迭 2������ �ٲٱ�

  //�ึ�� �� ĭ�� �� �迭 2�������� ���ϱ�
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      res[i][j] = cnt1[i][j] + cnt2[i][j];
    }
  }

  //�ึ�� �� ĭ�� ���� ���� 0���� ũ�� #, 0�̸� ���� �߰��ϱ�
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (res[i][j] > 0) {
        answer[i] += "#";
      } else answer[i] += " ";
    }
  }

  return answer;
}
