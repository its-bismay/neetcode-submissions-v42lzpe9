class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for point in points:
            [x, y] = point

            d = -1 * (x ** 2 + y ** 2) ** 0.5

            heapq.heappush(ans, (d, point))

            while len(ans) > k:
                heapq.heappop(ans)
        
        return [point for distance, point in ans]



        