class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')' : '(',
        ']':'[',
        '}': '{'}
        open_stack = []
        for bracket in s:
            if bracket in brackets:
                if open_stack and open_stack[-1] == brackets[bracket]:
                    open_stack.pop()
                else:
                    return False
            else:
                open_stack.append(bracket)
        return len(open_stack) == 0

        