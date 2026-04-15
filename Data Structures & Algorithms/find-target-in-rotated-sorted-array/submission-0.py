class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getminIdx (l, r):
            while l <= r:
                mid = l + ((r - l) // 2)

                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[r]:
                    r = mid
                else:
                    return mid
        l, r = 0, len(nums) - 1
        minIdx = getminIdx(l, r)

        if minIdx == 0:
            left = 0
            right = len(nums) - 1
        elif target >= nums[0] and target <= nums[minIdx - 1]:
            left = 0
            right = minIdx - 1
        else:
            left = minIdx
            right = len(nums) - 1
        
        while left <= right:
            m = left + ((right - left) // 2)

            if nums[m] > target:
                right = m - 1
            elif nums[m] < target:
                left = m + 1
            else:
                return m
        
        return -1
