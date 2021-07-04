from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.buildParenthesis(n, '', res, 0, 0)
        return res

    def buildParenthesis(self, n, built, res, open, close):
        if open == n and close == n:
            res.append(built)
            return

        if open < n:
            self.buildParenthesis(n, built + '(', res, open + 1, close)

        if close < open:  # if use close < n, we will have like ())(, which is illegal
            self.buildParenthesis(n, built + ')', res, open, close + 1)


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))