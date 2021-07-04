from typing import List


class Solution:
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        self.backTracking(digits, 0, '', res)
        return res

    def backTracking(self, digits, start, prefix, res):
        if len(prefix) == len(digits):
            res.append(prefix)
            return

        for key in self.mapping[digits[start]]:
            self.backTracking(digits, start + 1, prefix + key, res)

        # mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        #
        # if not digits: return []
        # if len(digits) == 1: return list(mapping[digits[0]])
        #
        # # combination
        # prev = mapping[digits[0]]
        # addings = self.letterCombinations(digits[1:])
        # return list((c + s) for c in prev for s in addings)