class Solution:
    def isPalindrome(self, x: int) -> bool:
        noInStr = str(x)

        l = 0
        r = len(noInStr) - 1

        while l <= r:
            if (noInStr[l] != noInStr[r]):
                return False
            l += 1
            r -= 1
        
        return True
        