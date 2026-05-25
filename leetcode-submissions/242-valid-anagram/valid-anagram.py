class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        sFreq = {}
        tFreq = {}
        for i in range(n):
            sFreq[s[i]] = 1 + sFreq.get(s[i], 0)
            tFreq[t[i]] = 1 + tFreq.get(t[i], 0)
        
        for ch in sFreq:
            if sFreq[ch] != tFreq.get(ch, 0):
                return False
        return True

