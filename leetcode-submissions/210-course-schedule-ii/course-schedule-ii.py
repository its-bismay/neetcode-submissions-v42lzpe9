class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        added = set()
        ans = []
        hmap = defaultdict(list)

        for course, prereq in prerequisites:
            hmap[course].append(prereq)

        def dfs(i):
            if i in visited:
                return False
            elif i in added:
                return True
            
            visited.add(i)
            for preq in hmap[i]:
                if not dfs(preq):
                    return False

            visited.remove(i)
            added.add(i)
            ans.append(i)
            return True 



        for i in range(numCourses):
                if not dfs(i):
                    return [] 
        
        return ans