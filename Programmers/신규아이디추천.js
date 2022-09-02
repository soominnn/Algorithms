function solution(new_id) {
  const pattern1 = /[0-9]/;
  const pattern2 = /[a-z]/;
  const pattern3 = /[-_.]/;

  //1
  new_id = new_id.toLowerCase();

  //2
  for (let word of new_id) {
    if (!pattern1.test(word) && !pattern2.test(word) && !pattern3.test(word))
      new_id = new_id.replace(word, "");
  }

  //3
  let st_new_id = new Array();
  for (let word of new_id) {
    if (!(word === "." && word === st_new_id.at(-1))) st_new_id.push(word);
  }
  new_id = st_new_id.join("");

  //4
  if (new_id[0] === ".") new_id = new_id.substring(1);
  if (new_id.at(-1) === ".") new_id = new_id.substring(0, new_id.length - 1);

  //5
  if (new_id === "") new_id = "a";

  //6
  if (new_id.length >= 16) {
    new_id = new_id.substring(0, 15);
    if (new_id.at(-1) === ".") new_id = new_id.substring(0, new_id.length - 1);
  }

  //7
  if (new_id.length <= 2) {
    const len = new_id.length;
    for (let i = 0; i < 3 - len; i++) {
      new_id += new_id.at(-1);
      console.log(new_id);
    }
  }
  let answer = new_id;
  return answer;
}
