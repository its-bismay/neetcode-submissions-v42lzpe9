class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prevSum = 0
        ans = []

        for num in nums:
            currSum = prevSum + num
            ans.append(currSum)
            prevSum = currSum
        
        return ans

        