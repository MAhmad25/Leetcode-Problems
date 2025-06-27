const firstUniqChar = function (s) {
    const countObj = {};
    for (const char of s) countObj[char] = (countObj[char] || 0) + 1;
    for (let i = 0; i < s.length; i++) {
        if (countObj[s[i]] === 1) return i;
    }
    return -1
};