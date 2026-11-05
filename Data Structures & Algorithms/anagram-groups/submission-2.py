from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for st in strs:
            key = [0] * 26
            for s in st:
                key[ord(s) - ord("a")] += 1
            hashMap[tuple(key)].append(st)
        
        return list(hashMap.values())
        