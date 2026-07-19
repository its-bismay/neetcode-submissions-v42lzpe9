class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        minHeap = [(0, 0)]
        total = 0
        while len(seen) < n:
            dist, idx = heapq.heappop(minHeap)

            if idx  in seen:
                continue
            
            seen.add(idx)

            total  = total + dist

            x_idx, y_idx = points[idx]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]

                    nei_dist = abs(x_idx - xj) + abs(y_idx - yj)

                    heapq.heappush(minHeap, (nei_dist, j))
        
        return total