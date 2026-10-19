class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        max_pdt = -float("inf")
        pre, suf = 1, 1
        for i in range(len(nums)):
            pre *= nums[i]
            suf *= nums[n-i-1]
            max_pdt = max(max_pdt, max(pre, suf))
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
        
        return max_pdt
        