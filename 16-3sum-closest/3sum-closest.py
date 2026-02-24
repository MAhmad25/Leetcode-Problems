class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closetSum = float('inf')
        n = len(nums)
        for index in range(n-2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            low = index+1
            high = n-1
            while (low < high):
                threeSum = nums[index] + nums[low]+nums[high]
                if threeSum == target:
                    return threeSum
                if abs(threeSum-target) < abs(closetSum-target):
                    closetSum=threeSum  
                if threeSum < target:
                    low += 1
                else:
                    high -= 1
        return closetSum