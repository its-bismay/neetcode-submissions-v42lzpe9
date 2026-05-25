class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq= {}
        ans = 0
        l = 0
        for r in range(len(s)):
            while s[r] in freq and freq[s[r]] > 0:
                freq[s[l]] -= 1
                l += 1
            freq[s[r]] = 1 + freq.get(s[r], 0)
            ans = max(ans, r - l + 1)
        return ans

        