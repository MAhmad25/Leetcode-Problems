function missingNumber(nums: number[]): number {
    const length: number = nums.length;
    const sum: number = nums.reduce((acc, currentVal) => acc + currentVal, 0);
    const sum_n_number:number = (length*(length+1))/2;
    return sum_n_number-sum;
};