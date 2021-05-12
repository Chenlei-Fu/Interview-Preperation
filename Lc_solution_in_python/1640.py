# Link: https://leetcode.com/problems/check-array-formation-through-concatenation/
# Author: Chenlei Fu

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {x[0]:x for x in pieces}
        print(d)
        res = []
        for num in arr:
            res += d.get(num, [])
        return res == arr