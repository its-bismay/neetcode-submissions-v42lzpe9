class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        t = len(s1)
        s = len(s2)

        if t > s:
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for i in range(t):
            count_s1[ord(s1[i]) - ord("a")] += 1
            count_s2[ord(s2[i]) - ord("a")] += 1  

        if count_s1 == count_s2:
            return True

        for i in range(t, s):
            count_s2[ord(s2[i]) - ord("a")] += 1
            count_s2[ord(s2[i - t]) - ord("a")] -= 1 

            if count_s1 == count_s2:
                return True
        return False
