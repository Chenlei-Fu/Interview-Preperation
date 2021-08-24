class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        S, l, r = list(s), 0, len(s) - 1
        while l < r:
            if not s[l].isalpha():
                l += 1
            elif not s[r].isalpha():
                r -= 1
            else:
                S[l], S[r] = S[r], S[l]
                r -= 1
                l += 1
        return ''.join(S)