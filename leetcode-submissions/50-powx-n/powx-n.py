class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1

            temp = helper(n//2)
            if n%2 == 0:
                return temp * temp
            else:
                return temp * temp * x
        ans = helper(abs(n))
        if n < 0:
            return 1/ans
        return ans
        