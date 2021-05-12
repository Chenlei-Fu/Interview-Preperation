from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        DP
        1. Sort the array. Ascend on width and descend on height if width are same.
        [3, 4] cannot contains [3, 3], so we need to put [3, 4] before [3, 3] when sorting otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]
        因为是greater than不是greater or equal to
        2. Find the longest increasing subsequence based on height.
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for width, height in envelopes:
            idx = bisect_left(dp, height)
            if idx == len(dp): # no value smaller than num
                dp.append(height)
            else:
                dp[idx] = height
        return len(dp)
        