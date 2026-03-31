class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freqList = [[] for i in range(len(nums) + 1)]
        res= []

        for n in nums:
            count[n] = 1 + count.get(n, 0) 
        
        for num, frequency in count.items():
            freqList[frequency].append(num)

        for i in range(len(freqList) - 1, 0, -1):
            for n in freqList[i]:
                if len(res) != k:
                    res.append(n)
                else:
                    return res
        return res
