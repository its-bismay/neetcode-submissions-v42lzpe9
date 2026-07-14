class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def findRoot(n):
            res = n

            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]

            return res
        
        def unionRoot(n1, n2):
            p1, p2 = findRoot(n1), findRoot(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2]  = p1
                rank[p1] += rank[p2]
            
            return 1
        
        for x1, x2 in edges:
            n -= unionRoot(x1, x2)
        
        return n
                

        