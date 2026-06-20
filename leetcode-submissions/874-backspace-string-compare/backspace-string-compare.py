class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stS = []
        stT = []

        for c in s:
            if c != "#":
                stS.append(c)
            elif len(stS) > 0:
                stS.pop()
                
        for c in t:
            if c != "#":
                stT.append(c)
            elif len(stT) > 0:
                stT.pop()
        
        return stS == stT
        