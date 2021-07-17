from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        '4' in row 7 is encoded as (4, 7)
        '4' in column 7 is encoded as (7, 4)
        '4' in the top-right block is encoded as (0, 4, 2)
        """
        seen = set()
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != ".":
                    for x in [(num, i), (j, num), (i//3, num, j//3)]:
                        if x in seen: return False
                        else: seen.add(x)
        return True