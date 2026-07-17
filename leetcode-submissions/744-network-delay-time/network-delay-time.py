class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)

        for u,v,w in times:
            adjList[u].append((w,v))
        
        minHeap = [(0, k)]
        t = 0
        visited = set()
        while minHeap:
            w1, v1 = heapq.heappop(minHeap)

            if v1 in visited:
                continue

            visited.add(v1)
            t = max(t, w1)

            for w2, v2 in adjList[v1]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, v2))
        
        return t if len(visited) == n else -1
        