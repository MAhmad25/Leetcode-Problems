class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def find_max_freq(freq):
            return freq.get(1, 0) if freq else 0
        low = 0
        freq = {}
        result = 0
        for high in range(len(nums)):
            freq[nums[high]] = freq.get(nums[high], 0)+1
            big_value_in_freq = find_max_freq(freq)
            win_len = high-low+1
            no_of_ch_replaceable = win_len-big_value_in_freq
            while no_of_ch_replaceable > k:
                freq[nums[low]] -= 1
                if freq[nums[low]] == 0:
                    del freq[nums[low]]
                low += 1
                big_value_in_freq = find_max_freq(freq)
                win_len = high-low+1
                no_of_ch_replaceable = win_len-big_value_in_freq
            result = max(result, high-low+1)
        return result