class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        prev = 1
        for idx, value in enumerate(nums):
            ans[idx] = prev
            prev = prev * value
        
        nxt = 1
        for idx in range(len(nums) - 1, -1, -1):
            ans[idx] *= nxt
            nxt *= nums[idx]
        
        return ans

        