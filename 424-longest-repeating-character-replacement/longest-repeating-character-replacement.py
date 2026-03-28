class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      def find_max(freq):
        return max(freq.values()) if freq else 0

      freq = {}
      low = 0
      res = 0

      for high in range(len(s)):
            ch = s[high]
            freq[ch] = freq.get(ch, 0) + 1

            ch_most_repeated = find_max(freq)
            length = high - low + 1
            character_to_replace = length - ch_most_repeated

            while character_to_replace > k:
                left_ch = s[low]
                freq[left_ch] -= 1
                if freq[left_ch] == 0:
                    del freq[left_ch]
                low += 1

                ch_most_repeated = find_max(freq)
                length = high - low + 1
                character_to_replace = length - ch_most_repeated

            res = max(res, high - low + 1)
      return res