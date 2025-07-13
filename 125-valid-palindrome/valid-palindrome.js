const isPalindrome = function (s) {
    const res = s.replace(/[^0-9a-zA-Z]/g, "").toLowerCase();
    let l = 0,
        h = res.length - 1;
    while (l < h) {
        if (res[l] !== res[h]) return false;
        h--;
        l++;
    }
    return true;
};