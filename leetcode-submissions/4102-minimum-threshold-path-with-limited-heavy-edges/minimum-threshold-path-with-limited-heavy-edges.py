from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        # If source and target are the same, no edges are traversed.
        if source == target:
            return 0
        
        # Build the adjacency list graph
        graph = defaultdict(list)
        max_weight = 0
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            if w > max_weight:
                max_weight = w
                
        # Helper function to check if a valid path exists for a given mid_threshold
        def isValid(threshold: int) -> bool:
            # dist[i] stores the minimum number of heavy edges to reach node i
            dist = [float('inf')] * n
            dist[source] = 0
            
            # Deque for 0-1 BFS
            queue = deque([source])
            
            while queue:
                u = queue.popleft()
                
                if u == target:
                    return dist[u] <= k
                
                for v, weight in graph[u]:
                    # Determine cost: 0 if light edge, 1 if heavy edge
                    cost = 0 if weight <= threshold else 1
                    
                    if dist[u] + cost < dist[v]:
                        dist[v] = dist[u] + cost
                        # 0-1 BFS optimization: 
                        # push to front if cost is 0, to back if cost is 1
                        if cost == 0:
                            queue.appendleft(v)
                        else:
                            queue.append(v)
                            
            return dist[target] <= k

        # Binary Search over the possible threshold values
        low, high = 0, max_weight
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid       # This threshold works, try to find a smaller one
                high = mid - 1
            else:
                low = mid + 1   # This threshold fails, we need a larger one
                
        return ans
        