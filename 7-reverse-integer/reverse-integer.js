const reverse = (x) => {
  const MAX =  2**31 - 1; 
  const MIN = -(2**31);
  const sign = Math.sign(x);
  const absStr = Math.abs(x).toString();
  const revStr = absStr.split("").reverse().join("");
  const revNum = sign * parseInt(revStr, 10);
  if (revNum > MAX || revNum < MIN) return 0;

  return revNum;
};