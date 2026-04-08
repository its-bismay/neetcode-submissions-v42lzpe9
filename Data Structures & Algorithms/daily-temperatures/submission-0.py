class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []

        for i in range(n):
            temp = temperatures[i]
            while stk and stk[-1][1] < temp:
                idx, val = stk.pop()
                res[idx] = i - idx
            stk.append((i, temp))
        
        return res