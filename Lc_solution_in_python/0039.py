from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backTracking(candidates, target, 0, [], res)
        return res

    def backTracking(self, candidates, target, start, tmp, res):
        if target < 0:
            return
        if target == 0:
            res.append(tmp)
            return
        for i in range(start, len(candidates)):
            self.backTracking(candidates, target - candidates[i], i, tmp + [candidates[i]], res)
