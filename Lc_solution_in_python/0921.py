class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left, right = 0, 0
        for p in S:
            if p == '(':
                left += 1
            elif p == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left + right
#         res, stack = 0, []
#         for p in S:
#             if p == '(':
#                 stack.append(p)

#             elif p == ')':
#                 if len(stack) == 0:
#                     res += 1
#                 else:
#                     stack.pop()
#         return res + len(stack)