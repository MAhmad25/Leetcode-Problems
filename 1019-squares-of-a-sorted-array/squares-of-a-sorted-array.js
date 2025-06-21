var sortedSquares = function(nums) {
const square = nums.map((num) => Math.abs(num) ** 2);
 return (square.sort((a, b) => a - b));
};