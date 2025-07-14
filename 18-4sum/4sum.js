const fourSum = (nums, target) => {
    const master = [];
    nums = nums.sort((a, b) => a - b);
    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;
        for (let j = i + 1; j < nums.length;) {
            let low = j + 1,
                high = nums.length - 1;
            while (low < high) {
                const sum = nums[i] + nums[j] + nums[low] + nums[high];
                if (sum < target) low++;
                else if (sum > target) high--;
                else {
                    master.push([nums[i], nums[j], nums[low], nums[high]]);
                    low++;
                    high--;
                    while (low < high && nums[low] === nums[low - 1]) low++;
                    while (low < high && nums[high] === nums[high + 1]) high--;
                }
            }
            j++;
            while (j < nums.length && nums[j] === nums[j - 1]) j++;
        }
    }
    return master;
};
const nums = [1, 0, -1, 0, -2, 2];
console.log(fourSum(nums, 0));
