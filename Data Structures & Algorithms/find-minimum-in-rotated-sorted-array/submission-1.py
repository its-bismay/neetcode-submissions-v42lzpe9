class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = float("infinity")
        while l <= r:
            if nums[l] < nums[r]:
                minVal = min(minVal, nums[l])
                break
            
            m = l + ((r - l) // 2)
            minVal = min(minVal, nums[m])

            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m - 1
        
        return minVal
        