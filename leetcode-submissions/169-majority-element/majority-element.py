class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        freq_arr = list(freq.items())
        freq_arr.sort(key=lambda x: x[1])
        return freq_arr[-1][0]