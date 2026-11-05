class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sFreq = {}
        tFreq = {}
        for i in range(len(s)):
            sFreq[s[i]] = 1 + sFreq.get(s[i], 0)
            tFreq[t[i]] = 1 + tFreq.get(t[i], 0)
        
        for key in sFreq:
            if sFreq[key] != tFreq.get(key, 0):
                return False
        
        return True
        

        