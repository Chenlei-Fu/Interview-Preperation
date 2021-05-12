class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """
        solution 1
        """
        cmax = 0
        for i in range(len(A)-2):
            cmax = max(cmax, A[i])
            if cmax > A[i+2]:
                return False
        return True

        """
        solution 2
        """
        return all([abs(a-i)<=1 for i, a in enumerate(A)])
        # for i, a in enumerate(A):
        #     if abs(a - i) > 1:
        #         return False
        # return True