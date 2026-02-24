class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for index in range(n - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            low = index + 1
            high = n - 1
            target = -1 * nums[index]
            while low < high:
                twoSum = nums[low] + nums[high]
                if twoSum == target:
                    result.append([nums[index], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < n and nums[low] == nums[low - 1]:
                        low += 1
                    while high >= 0 and nums[high] == nums[high + 1]:
                        high -= 1
                elif twoSum < target:
                    low += 1
                else:
                    high -= 1

        return result
