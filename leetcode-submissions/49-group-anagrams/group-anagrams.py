class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for string in strs:
            sl = sorted(string)
            ss = "".join(sl)
            if ss in freq:
                freq[ss].append(string)
            else:
                freq[ss] = [string]
        
        return list(freq.values())


        