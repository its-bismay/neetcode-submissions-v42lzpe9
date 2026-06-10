class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        freq_arr = [[] for _ in range(len(nums)+1)]
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for num, count in freq.items():
            freq_arr[count].append(num)
        
        ans = []
        for i in range (len(freq_arr)-1, 0, -1):
            for n in freq_arr[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans


        