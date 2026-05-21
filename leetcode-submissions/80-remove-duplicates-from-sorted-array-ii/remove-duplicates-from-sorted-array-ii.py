class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n
        l = 1

        for r in range(2, len(nums)):
             if nums[r] != nums[l - 1]:
                nums[l+1] = nums[r]
                l += 1
        return l + 1        