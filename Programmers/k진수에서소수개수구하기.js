//�Ҽ� �Ǻ� �Լ�
const isPrime = (item) => {
  if (Number(item) < 2) {
    return false;
  }
  if (Number(item === 2)) {
    return true;
  }
  for (let i = 2; i <= Math.sqrt(item); i++) {
    if (Number(item) % i === 0) {
      return false;
    }
  }
  return true;
};

function solution(n, k) {
  let changeToK = "";
  let answer = 0;

  //k������ �ٲٱ�
  while (n !== 0) {
    let remainer = n % k;
    n = parseInt(n / k);
    changeToK = remainer + changeToK;
  }

  //0�� �������� ������
  changeToK = changeToK.split("0");

  changeToK.forEach((item) => {
    if (isPrime(item) === true) answer += 1;
  });

  return answer;
}
