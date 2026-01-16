class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index in range(len(nums)):
            currValue=nums[index]
            diff=target-currValue
            if diff in dict:
                return [dict[diff],index]
            else: dict[currValue]=index    
