class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        targetDict = {}
        for ch in t:
            targetDict[ch] = 1 + targetDict.get(ch, 0)
        
        sfreq = {}
        l = 0
        target, have = len(targetDict), 0
        res, resLen = [-1, -1], float("infinity") 
        for r in range(len(s)):
            c = s[r]
            sfreq[c] = 1 + sfreq.get(c, 0)
            if c in targetDict and sfreq[c] == targetDict[c]:
                have += 1
            
            while have == target:
                if (r - l + 1) < resLen:
                    resLen = (r - l + 1)
                    res = [l, r]
                
                sfreq[s[l]] -= 1
                if s[l] in targetDict and sfreq[s[l]] < targetDict[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""


                




        