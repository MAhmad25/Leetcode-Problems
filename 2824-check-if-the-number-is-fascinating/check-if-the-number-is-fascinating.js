var isFascinating = function (n) {
    let oneN = n.toString();
    let twoN = n * 2;
    let threeN = n * 3;
    let res = oneN + twoN + threeN;
    const arr = res.split("");
    arr.sort((a, b) => a - b);
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] === arr[i + 1]) return false;
    }
    return res.includes(0) ? false : true;
}