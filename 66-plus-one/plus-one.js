const plusOne = function (digits) {
    let str = digits.join("");
    let num = BigInt(str);
    num++;
    str = Array.from(num.toString());
    return str.map((num) => Number(num));
};