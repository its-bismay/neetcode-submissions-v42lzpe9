class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        carry = 0
        ans = []

        while n1 >= 0 or n2 >= 0 or carry:
            d1 = int(num1[n1]) if n1 >= 0 else 0
            d2 = int(num2[n2]) if n2 >= 0 else 0

            total = d1 + d2 + carry

            carry = total // 10
            total %= 10

            ans.append(str(total))

            n1 -= 1
            n2 -= 1

        return "".join(ans[::-1])