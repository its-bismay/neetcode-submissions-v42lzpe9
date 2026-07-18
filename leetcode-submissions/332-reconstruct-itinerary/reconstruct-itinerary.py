from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. Build the adjacency list with destinations sorted in reverse alphabetical order
        adj = defaultdict(list)
        
        # Sorting the tickets first ensures alphabetical order
        for src, dst in sorted(tickets):
            adj[src].append(dst)
            
        # Reverse the lists so we can use O(1) pop() from the end
        for src in adj:
            adj[src].reverse()

        res = []

        # 2. Post-order DFS to find the Eulerian path
        def dfs(src):
            while adj[src]:
                # Always take the lexicographically smallest available destination
                next_dst = adj[src].pop()
                dfs(next_dst)
            # Add to result only when we are stuck (no more outgoing flights)
            res.append(src)

        dfs("JFK")
        
        # 3. Reverse the result since post-order builds it backwards
        return res[::-1]
        