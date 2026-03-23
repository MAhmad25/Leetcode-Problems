class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low,sum=0,0
        min_len=float("inf")
        for high in range(len(nums)):
            sum+=nums[high]
            while sum>=target:
                size=high-low+1
                min_len=min(min_len,size)
                sum-=nums[low]
                low+=1
        return 0 if min_len==float("inf") else min_len