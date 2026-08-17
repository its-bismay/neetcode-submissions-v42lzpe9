class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(a):
            if a == n:
                return 1
            elif a > n:
                return 0

            if a in memo:
                return memo[a]

            memo[a] = dfs(a+1) + dfs(a+2)
            return memo[a]
        
        return dfs(0)



        