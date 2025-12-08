function singleNumber(nums: number[]): number {
    const count:Object = {};
    for (const char of nums) count[char] = (count[char] || 0) + 1;
    for (const [number, freq] of Object.entries(count)) if (freq === 1) return Number(number);
};