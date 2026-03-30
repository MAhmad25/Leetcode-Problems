class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for ch in t:
            count[ch] = count.get(ch, 0) + 1
        
        need = len(t)
        left = 0
        ans = ""
        
        for right in range(len(s)):
            if s[right] in count:
                if count[s[right]] > 0:
                    need -= 1
                count[s[right]] -= 1
            
            while need == 0:
                if ans == "" or right-left+1 < len(ans):
                    ans = s[left:right+1]
                
                if s[left] in count:
                    count[s[left]] += 1
                    if count[s[left]] > 0:
                        need += 1
                
                left += 1
        
        return ans