from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        carry method for adding is to check whether it's smaller than nine
        because nine plus one should be carried.
        If we find any digits that smaller than 9,
        the carrying has been terminated and we should return.

        :param digits: array list
        :return: array list
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits