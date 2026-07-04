class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(curr):
            if curr >= len(nums):
                ans.append(subset[:])
                return
            subset.append(nums[curr])
            dfs(curr + 1)
            subset.pop()
            dfs(curr + 1)
        
        dfs(0)
        return ans


        