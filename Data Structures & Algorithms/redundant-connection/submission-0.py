class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rank = [1] * (len(edges) + 1)
        nodes = [i for i in range(len(edges) + 1)]

        def findroot(node):
            res = node
            while res != nodes[res]:
                nodes[res] = nodes[nodes[res]]
                res = nodes[res]
            
            return res

        def union(n1, n2):
            p1, p2 = findroot(n1), findroot(n2)

            if p1 == p2:
                return False
            
            if rank[p2] > rank[p1]:
                nodes[p1] = p2
                rank[p2] += rank[p1]
            else:
                nodes[p2] = p1
                rank[p1] += rank[p2]
            
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        