# from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strDict = defaultdict(list)

        for ch in strs:
            sortedStr = "".join(sorted(ch))
            strDict[sortedStr].append(ch)
        
        return list(strDict.values())

        