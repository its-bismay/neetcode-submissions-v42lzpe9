class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = 0
        lower = 0

        for ch in word:
            if ord("A") <= ord(ch) <= ord("Z"):
                upper += 1
            else:
                lower += 1
        
        n = len(word)

        if upper == n:
            return True
        
        if lower == n:
            return True
        
        if word[0].isupper() and n - 1 == lower:
            return True
        
        return False


