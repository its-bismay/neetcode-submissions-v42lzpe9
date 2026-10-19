class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum, curr_sum, i = -float("inf"), 0, 0

        while i < len(nums):
            
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

            i += 1
        
        return max_sum
             
        