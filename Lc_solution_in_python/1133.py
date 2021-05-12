import collections
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        c = collections.Counter(A)
        return max([x for x in c if c[x] == 1] + [-1])