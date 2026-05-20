class Solution:
    def tribonacci(self, n: int) -> int:
        temp = {}

        def solve(m):
            if m == 0 or m == 1:
                return m
            if m == 2:
                return 1
            if m in temp:
                return temp[m]
            
            temp[m] = solve(m-1) + solve(m-2) + solve(m-3)
            return temp[m]
        
        return solve(n)
            
        