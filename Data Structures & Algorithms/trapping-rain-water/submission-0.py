class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1

        Lmax, Rmax, ans = 0, 0, 0

        while l < r:
            Lmax = max(Lmax, height[l])
            Rmax = max(Rmax, height[r])

            if Lmax <= Rmax :
                ans += Lmax - height[l]
                l += 1
            
            if Rmax < Lmax:
                ans += Rmax - height[r]
                r -= 1
        
        return ans


            
        