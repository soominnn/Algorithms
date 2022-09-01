function solution(id_list, report, k) {
  let answer = new Array(id_list.length).fill(0);
  const noneDupReport = [...new Set(report)];
  const reportList = {};

  id_list.map((user) => {
    reportList[user] = [];
  });

  noneDupReport.map((user) => {
    const [reporter, receiver] = user.split(" ");
    reportList[receiver].push(reporter);
  });

  for (const key in reportList) {
    if (reportList[key].length >= k) {
      reportList[key].map((user) => {
        answer[id_list.indexOf(user)] += 1;
      });
    }
  }
  return answer;
}
