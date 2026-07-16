class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        adjList = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adjList[pattern].append(word)
        
        q = deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)

        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adjList[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                            
            res += 1
        
        return 0
                


