class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set()
        def isTree(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for nei in adjList[i]:
                if nei == prev:
                    continue
                if not isTree(nei, i):
                    return False
            
            return True
        
        return isTree(0, -1) and n==len(visited)


        