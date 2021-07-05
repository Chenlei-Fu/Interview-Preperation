from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        generate the sequence iteratively:
        get n = i+1 by n = i
        the result is even!!
        """
        res = [0]
        for i in range(n):
            inc = 1 << i
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] + inc)
        return res