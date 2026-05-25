class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for idx, num in enumerate(nums):
            req = target - num
            if req in store:
                return [store[req], idx]
            store[num] = idx
        
        return []
        