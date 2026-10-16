class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for idx, num in enumerate(nums):
            req = target - num

            if req in seen:
                return [idx, seen[req]]
            
            seen[num] = idx



        