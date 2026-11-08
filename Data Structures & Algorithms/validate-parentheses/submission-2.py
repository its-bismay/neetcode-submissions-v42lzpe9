class Solution:
    def isValid(self, s: str) -> bool:
        charDict = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for ch in s:
            if ch in charDict:
                if stack and stack[-1] == charDict[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False

        