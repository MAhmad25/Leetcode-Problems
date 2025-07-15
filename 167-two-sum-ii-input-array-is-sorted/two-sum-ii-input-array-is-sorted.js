/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
const twoSum = function (numbers, target) {
    let low = 0,
        high = numbers.length - 1;
    while (low < high) {
        const sum = numbers[low] + numbers[high];
        if (sum < target) low++;
        else if (sum > target) high--;
        else return [low + 1, high + 1];

    }
};