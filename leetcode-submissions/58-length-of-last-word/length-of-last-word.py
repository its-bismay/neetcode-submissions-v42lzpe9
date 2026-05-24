class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        word = arr[-1]

        return len(word)
        