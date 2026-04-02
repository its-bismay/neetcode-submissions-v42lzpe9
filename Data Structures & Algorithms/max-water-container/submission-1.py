class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxV = 0

        while l < r:
            currV = min(heights[l], heights[r]) * (r - l)
            maxV = max(maxV, currV)

            if (heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1
        
        return maxV
