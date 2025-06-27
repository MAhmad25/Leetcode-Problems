const isPalindrome = function (s) {
    const regex = s.replace(/[^0-9a-zA-Z]/g, "");
    return regex.toLowerCase() === regex.split("").reverse().join("").toLowerCase()
};