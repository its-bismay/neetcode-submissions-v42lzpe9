class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                lastTemp, lastIdx = stack.pop()
                ans[lastIdx] = idx - lastIdx
            stack.append([temp, idx])
        
        return ans


        