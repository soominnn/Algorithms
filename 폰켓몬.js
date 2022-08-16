function solution(nums) {
  const n = nums.length / 2;
  const setNums = new Set(nums);
  let answer = 0;

  if (n >= [...setNums].length) answer = [...setNums].length;
  else answer = n;

  return answer;
}
