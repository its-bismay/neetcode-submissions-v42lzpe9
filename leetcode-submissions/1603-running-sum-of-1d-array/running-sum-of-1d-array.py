class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prevSum = 0
        ans = []

        for num in nums:
            prevSum = prevSum + num
            ans.append(prevSum)
        
        return ans

        