function twoSum(nums: number[], target: number): number[] {
    const obj = {};
    for (let i = 0; i < nums.length; i++) {
        let n = nums[i];
        if (obj[target - n]>=0) {
            return [obj[target - n], i];
        } else obj[n] = i;
    }
};