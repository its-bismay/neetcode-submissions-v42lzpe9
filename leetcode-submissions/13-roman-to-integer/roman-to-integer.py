class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0
        i = 0
        while i < (len(s)):
            if i < len(s) - 1 and romanDict[s[i]] < romanDict[s[i+1]]:
                ans += (romanDict[s[i+1]] - romanDict[s[i]])
                i += 2
            else:
                ans += romanDict[s[i]]
                i += 1

        
        return ans

        