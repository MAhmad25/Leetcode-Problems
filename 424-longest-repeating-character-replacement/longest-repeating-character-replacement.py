class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def find_max_freq(freq):
            return max(freq.values()) if freq else 0
        low=0
        freq={}
        result=0
        for high in range(len(s)):
            freq[s[high]]=freq.get(s[high],0)+1
            big_value_in_freq=find_max_freq(freq)
            win_len=high-low+1
            no_of_ch_replaceable=win_len-big_value_in_freq    
            while no_of_ch_replaceable>k:
                freq[s[low]]-=1
                if freq[s[low]]==0:
                    del freq[s[low]]
                low+=1
                big_value_in_freq=find_max_freq(freq)
                win_len=high-low+1
                no_of_ch_replaceable=win_len-big_value_in_freq
            result=max(result,high-low+1)
        return result                        