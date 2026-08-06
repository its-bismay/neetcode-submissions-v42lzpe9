class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        result = r

        while l <= r:
            m = l + ((r - l) // 2)
            currHour = 0
            for pile in piles:
                currHour = currHour + math.ceil(pile / m)
            
            if currHour <= h:
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1
        
        return result
        
        