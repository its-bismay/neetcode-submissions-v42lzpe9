class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        INT_MIN = -(2**31)
        INT_MAX = (2**31) - 1
        num = abs(x)
        rev_num = 0
        while num > 0:
            ld = num % 10
            rev_num = rev_num * 10 + ld
            num = num // 10

        rev_num *= sign

        if rev_num < INT_MIN or rev_num > INT_MAX:
            return 0
        
        return rev_num