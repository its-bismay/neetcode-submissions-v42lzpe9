class Solution:
    def isAlphanums(self, ch):
        if ord("a") <= ord(ch) <= ord("z"):
            return True
        elif ord("A") <= ord(ch) <= ord("Z"):
            return True
        elif ord("0") <= ord(ch) <= ord("9"):
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l < r and not self.isAlphanums(s[l]):
                l += 1
            while l < r and not self.isAlphanums(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True

        