class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                idx,lastH = stk.pop()
                width = i - idx
                res = max(res, (width * lastH))
                start = idx
            stk.append((start, h))
        
        while stk:
            idx,height = stk.pop()
            width = n - idx
            res = max(res, (width * height))
        
        return res

        