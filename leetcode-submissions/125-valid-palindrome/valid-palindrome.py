class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphanumeric (ch):
            if (ord("a") <= ord(ch) <= ord("z")) or (ord("0") <= ord(ch) <= ord("9")):
                return True
            return False

        s = s.lower()

        l = 0
        r = len(s) - 1

        while l < r:
            if not isAlphanumeric(s[l]):
                l += 1
            elif not isAlphanumeric(s[r]):
                r -= 1

            elif s[r] != s[l]:
                return False
            else:
                l += 1
                r -= 1
        
        return True

        