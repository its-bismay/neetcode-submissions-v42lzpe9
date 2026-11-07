class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charWindow = set()
        l = 0
        maxWindow = 0
        for r in range(len(s)):
            while s[r] in charWindow:
                charWindow.remove(s[l])
                l += 1
            
            charWindow.add(s[r])
            maxWindow = max(maxWindow, len(charWindow))
        
        return maxWindow



        