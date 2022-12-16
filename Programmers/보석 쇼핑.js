function solution(gems) {
    let answer = [0, gems.length];
    let start = 0;
    let end = 0;
    
    const gemKinds = new Set(gems).size;
    const collect = new Map();
    collect.set(gems[0], 1);
    
    while (start < gems.length && end < gems.length) {
        if (collect.size === gemKinds) {
            if (end - start < answer[1] - answer[0]) {
                answer = [start + 1, end + 1];
            }
            
            collect.set(gems[start], collect.get(gems[start]) -1);
            if (collect.get(gems[start]) === 0) {
                collect.delete(gems[start]);
            }
            start += 1;
        } else {
            end += 1;
            collect.set(gems[end], 1 + (collect.get(gems[end]) || 0));
        }
    }
    
    return answer;
}

// function solution(gems) {
//     let setGems = [...new Set(gems)];
//     let result = [0, gems.length];
//     start = 0 
//     end = 0
//     while (end < gems.length) {
//         let existGems = gems.slice(start, end + 1);
//         if ([...new Set(existGems)].length === setGems.length) {
//             let [s, d] = result;
//             if (d - s > end - start) {
//                 result = [start + 1, end + 1];   
//             }
//             start += 1;
//         } else {
//             end += 1;
//         }
//     }

//     return result;
// }