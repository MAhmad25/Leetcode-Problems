class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low,high=0,len(numbers)-1
        while(low<high):
            sum=numbers[low]+numbers[high]
            if sum==target:
                return [low+1,high+1]
            elif sum>target:
                high=high-1    
            elif sum<target:
                low=low+1