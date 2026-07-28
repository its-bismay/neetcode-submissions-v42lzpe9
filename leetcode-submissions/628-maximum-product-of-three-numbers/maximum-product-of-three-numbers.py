class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        total = 1

        for i in range(n-3, n):
            total = total * nums[i]
        
        if nums[0] * nums[1] * nums[-1] >= total:
            return nums[0] * nums[1] * nums[-1]

        else: return total

        