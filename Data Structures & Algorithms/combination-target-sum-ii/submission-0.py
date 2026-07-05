class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        res, sol = [], []

        n = len(nums)

        def dfs(i, total):
            if total == target:
                res.append(sol[:])
                return
            if i == n or total > target:
                return
            
            sol.append(nums[i])
            dfs(i+1, total + nums[i])

            sol.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res        