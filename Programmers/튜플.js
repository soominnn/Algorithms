function solution(s) {
  let answer = [];

  //���ڿ� ������ ��ҵ� ���̿� ���� �������� ����
  s = s
    .slice(2, -2)
    .split("},{")
    .sort((a, b) => {
      if (a.length > b.length) return 1;
      if (a.length < b.length) return -1;
    });

  //��ǥ�� �ѹ� �� ������ answer�� ���� �͵鸸 �����ؼ� answer�� �ֱ�
  for (let item of s) {
    item = item.split(",");
    for (let i = 0; i < item.length; i++) {
      if (answer.includes(parseInt(item[i])) === false)
        answer.push(parseInt(item[i]));
    }
  }

  return answer;
}
