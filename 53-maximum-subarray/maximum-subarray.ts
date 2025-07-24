function maxSubArray(nums: number[]): number {
    let maxSum: number = -Infinity;
    let currSum: number = 0;
    for (const val of nums) {
        currSum += val;
        maxSum = Math.max(currSum, maxSum);
        if (currSum < 0) currSum = 0;
    }
    return maxSum;
}