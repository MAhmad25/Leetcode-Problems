function singleNumber(nums: number[]): number {
    let xor: number = 0;
    for (let i: number = 0; i < nums.length; i++) {
        xor = xor ^ nums[i];
    }
    return xor;
};