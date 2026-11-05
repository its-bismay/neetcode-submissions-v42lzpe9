class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestSeq = 0
        for num in nums:
            if num - 1 not in numsSet:
                currSeq = 0
                while num in numsSet:
                    currSeq += 1
                    num = num + 1
                
                longestSeq = max(longestSeq , currSeq)
        
        return longestSeq
        