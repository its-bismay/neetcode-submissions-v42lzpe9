class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n-2):
            if s[i] != s[i+1] and s[i+1] != s[i+2] and s[i] != s[i+2]:
                ans += 1
        return ans