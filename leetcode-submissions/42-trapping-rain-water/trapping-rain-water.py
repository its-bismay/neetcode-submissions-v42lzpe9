class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = 0, 0
        v_water = 0
        while l < r:
            if height[l] <= height[r]:
                if max_l > height[l]:
                    v_water += (max_l- height[l])
                else:
                    max_l = height[l]
                l += 1
            else:
                if max_r > height[r]:
                    v_water += (max_r - height[r])
                else:
                    max_r = height[r]
                r -= 1
        
        return v_water
        



        