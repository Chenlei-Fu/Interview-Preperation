# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# author: chenlei fu
# time complexity: O(N)
# space complexity: O(1)

from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # not in-build function
        arr_idx1, arr_idx2, str_idx1, str_idx2 = 0, 0, 0, 0
        while arr_idx1 < len(word1) and arr_idx2 < len(word2):
            if word1[arr_idx1][str_idx1] != word2[arr_idx2][str_idx2]:
                return False
            if str_idx1 >= len(word1[arr_idx1]) - 1:
                str_idx1 = 0
                arr_idx1 += 1
            else:
                str_idx1 += 1
            if str_idx2 >= len(word2[arr_idx2]) - 1:
                str_idx2 = 0
                arr_idx2 += 1
            else:
                str_idx2 += 1
        return arr_idx1 == len(word1) and arr_idx2 == len(word2)

        # with built-in function

        # return ''.join(word1) == ''.join(word2)

if __name__ == '__main__':
    s = Solution()
    print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))