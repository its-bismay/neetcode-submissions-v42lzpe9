class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        el1, el2, cnt1, cnt2 = -float("inf"), -float("inf") , 0 , 0

        for i in range(len(nums)):
            if cnt1 == 0 and nums[i] != el2:
                el1 = nums[i]
                cnt1 = 1
            elif cnt2 == 0 and nums[i] != el1:
                el2 = nums[i]
                cnt2 = 1
            elif nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        ans = []
        cnt1, cnt2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1
        target = len(nums) // 3
        if cnt1 > target:
            ans.append(el1)
        if cnt2 > target:
            ans.append(el2)
        
        return ans