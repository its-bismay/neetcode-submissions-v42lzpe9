class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def dfs(k):
            if k == n:
                return 1
            if k > n:
                return 0
            
            if k in memo:
                return memo[k]

            memo[k] = dfs(k+1) + dfs(k+2)
            return memo[k]
        
        return dfs(0)

        