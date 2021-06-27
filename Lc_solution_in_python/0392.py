class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        indexS, indexT = 0, 0
        while indexT < len(t):
            if t[indexT] == s[indexS]:
                indexS += 1
                if indexS == len(s): return True
            indexT += 1
        return False

    # def isSubsequence(self, s: str, t: str) -> bool:
    #     """
    #     O(logn) solution: binary search
    #     """
    #     idx = defaultdict(list)
    #     for i, c in enumerate(t):
    #         idx[c].append(i)
    #     prev = 0  # prev location of t that other matching can exists in
    #     for i, c in enumerate(s):
    #         j = bi.bisect_left(idx[c], prev)
    #         if j == len(idx[c]): return False  # not exists
    #         prev = idx[c][j] + 1
    #     return True

"""
Subsequence of string must be in the same order
no matter the number of subsequences there is
"""