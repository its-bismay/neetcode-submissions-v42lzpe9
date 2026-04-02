class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlnum (ch: str) -> bool:
            val = ord(ch)
            if ord("a") <= val <= ord("z"):
                return True
            if ord("A") <= val <= ord("Z"):
                return True
            if ord("0") <= val <= ord("9"):
                return True
            return False
        
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isAlnum(s[l]):
                l += 1
            while l < r and not isAlnum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True


        