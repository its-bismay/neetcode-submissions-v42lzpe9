class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix, prefix = [1] * n, [1] * n

        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        ans = []
        i = 0
        while i < n:
            ans.append(suffix[i] * prefix[i])
            i += 1
        return ans


