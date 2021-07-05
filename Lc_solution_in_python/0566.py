from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        if r * c != m * n: return mat
        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r * c):
            res[i // c][i % c] = mat[i // m][i % m]
        return res