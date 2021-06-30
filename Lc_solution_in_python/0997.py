from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        judge: indegree = n, outdegree = 0
        """
        degs = defaultdict(int)
        for peer in trust:
            degs[peer[0]] -= 1
            degs[peer[1]] += 1

        for i in range(1, n + 1):
            if degs[i] == n - 1:
                return i
        return -1