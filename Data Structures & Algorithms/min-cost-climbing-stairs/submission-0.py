class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: 
        n = len(cost)
        memo = {}
        def dfs(a):
            if a == n:
                return 0
            elif a > n:
                return float("inf")

            if a in memo:
                return memo[a]

            memo[a] = min((cost[a] + dfs(a+1)), (cost[a] + dfs(a+2)))
            return memo[a]
        
        return min(dfs(0), dfs(1))
        