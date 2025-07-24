function maxSubArray(nums: number[]): number {
    let maxSum: number = -Infinity;
    let currSum: number = 0;
    for (let i: number = 0; i < nums.length; i++) {
        currSum += nums[i];
        maxSum = Math.max(currSum, maxSum);
        if (currSum < 0) currSum = 0;
    }
    return maxSum;
}