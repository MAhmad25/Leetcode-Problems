function missingNumber(nums: number[]): number {
    const length: number = nums.length;
    let sum: number = 0;
    for (let i: number = 0; i < nums.length; i++)sum += nums[i];
    const sum_n_number: number = (length * (length + 1)) / 2;
    return sum_n_number - sum;
};