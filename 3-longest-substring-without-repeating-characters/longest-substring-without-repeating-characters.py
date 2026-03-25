class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        low = 0
        max_len = 0
        freq = {}
        for high in range(n):
            freq[s[high]] = freq.get(s[high], 0)+1
            k = high-low+1
            while len(freq) < k:
                freq[s[low]] -= 1
                if freq[s[low]] == 0:
                    del freq[s[low]]
                low += 1
                k = high-low+1
            size = high-low+1
            max_len = max(max_len, size)
        return max_len