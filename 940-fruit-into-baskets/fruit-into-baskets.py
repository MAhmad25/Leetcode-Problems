class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        low=0
        max_len=1
        freq={}
        for high in range(n):
            freq[fruits[high]]=freq.get(fruits[high],0)+1
            while len(freq)>2:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
            if len(freq)<=2:
                size=high-low+1
                max_len=max(max_len,size)
        return max_len        