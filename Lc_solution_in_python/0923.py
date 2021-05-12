import collections
import itertools
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        """
        O(n^2) -- slow but straightforward
        """
        # twosums, res = {}, 0
        # for i in range(len(arr)):
        #     res += twosums.get(target - arr[i], 0)
        #     for j in range(i):
        #         twosums[arr[i] + arr[j]] = twosums.get(arr[i] + arr[j], 0) + 1
        # return res%(10**9 + 7)

        """
        O(N^2) 
        """
       
        c = collections.Counter(arr)
        res = 0
        for i, j in itertools.combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: # C_n^3
                res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j and j != k:
                res += c[i] * (c[i] - 1)//2 * c[k]
            elif k > i and k > j:
                res += c[i] * c[j] * c[k]
        return res % (10**9 + 7)
                
            