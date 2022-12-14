const bfs = (start, nodes, visited, distance) => {
    const queue = [[start, 0]];
    visited[start] = true;
    while (queue.length > 0) {
        const [findNode, dis] = queue.shift();
        for (let i = 0; i < nodes[findNode].length; i++){
            if (visited[nodes[findNode][i]] === false) {
                queue.push([nodes[findNode][i], dis + 1]);
                visited[nodes[findNode][i]] = true;
                distance[nodes[findNode][i]] = dis + 1;
            }
        }
    }
}

function solution(n, edge) {
    const visited = Array(n + 1).fill(false);
    const distance = Array(n + 1).fill(0);
    const nodes = Array.from(Array(n + 1), () => Array(0));
    let count = 0;
    edge.forEach(e => {
        const left = e[0];
        const right = e[1];
        nodes[left].push(right);
        nodes[right].push(left);
    })
    bfs(1, nodes, visited, distance);
    const maxDistance = Math.max(...distance);
    distance.forEach((d,i) => {if (d === maxDistance) count += 1;})

    return count;
}