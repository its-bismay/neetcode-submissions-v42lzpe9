class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for ch in s :
            freq[ch] = 1 + freq.get(ch, 0)
        
        for idx,ch in enumerate(s):
            if freq[ch] == 1:
                return idx
        return -1




        