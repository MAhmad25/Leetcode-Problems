class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 256
        left = 0
        res = 0

        def find_max(arr):
            return max(arr)

        for right in range(len(s)):
            freq[ord(s[right])] += 1

            maxcnt = find_max(freq)
            length = right - left + 1
            diff = length - maxcnt

            while diff > k:
                freq[ord(s[left])] -= 1
                left += 1
                maxcnt = find_max(freq)
                length = right - left + 1
                diff = length - maxcnt

            res = max(res, right - left + 1)

        return res