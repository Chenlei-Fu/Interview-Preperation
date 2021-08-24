class Solution:
    def calculate(self, s: str) -> int:
        stack, sign, number, res = [], 1, 0, 0
        for c in s:
            if c.isdigit():
                number = number*10 + int(c)
            elif c == '+' or c == '-':
                res += sign * number
                sign = 1 if c == '+' else -1
                number = 0
            elif c == '(': #push to stack to save
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * number
                number = 0
                res *= stack.pop()
                res += stack.pop()
        if number != 0:
            res += sign * number
        return res
                