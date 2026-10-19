class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        el = nums[0]
        cnt = 0

        for i in range(len(nums)):
            if cnt == 0:
                el = nums[i]
                cnt += 1
            elif nums[i] == el:
                cnt += 1
            else:
                cnt -= 1
        el_cnt = 0
        for num in nums:
            if num == el:
                el_cnt += 1
        
        if el_cnt > len(nums) // 2:
         return el 
        else:
            return -1

        


        
        