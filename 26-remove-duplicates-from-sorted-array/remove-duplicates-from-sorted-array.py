class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique=0
        officer=0
        for cm in range(1,len(nums)):
            if nums[officer]!=nums[cm]:
                unique=unique+1
                nums[officer+1]=nums[cm]
                officer=officer+1
        return unique+1