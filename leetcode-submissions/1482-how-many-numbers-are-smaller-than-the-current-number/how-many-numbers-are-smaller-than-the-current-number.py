class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)
        freq = {}
        for i, n in enumerate(sorted_nums):
            if n not in freq:
                freq[n] = i
        ans = []
        for num in nums:
            ans.append(freq[num])

        return ans





        

        