# https://leetcode.com/problems/palindrome-permutation/
# Author: chenlei fu
# time complexity: O(N)
# space complexity: O(N)


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if s is None:
            return True
        mp = set()
        for c in s:
            if c in mp:
                mp.remove(c)
            else:
                mp.add(c)
        return len(mp) == 1 or len(mp) == 0