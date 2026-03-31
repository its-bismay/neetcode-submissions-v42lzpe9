class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len (t):
            return False
            
        charDict = {}

        for c in s:
            charDict[c] = 1 + charDict.get(c, 0)
        
        for ch in t:
            if ch not in charDict:
                return False
            charDict[ch] = charDict[ch] - 1
        
        if all(v == 0 for v in charDict.values()):
            return True
        else:
            return False
        

        