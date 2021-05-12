class Solution:
    def removePalindromeSub(self, s: str) -> int:
        """
        We can delete all characters 'a' in the 1st operation,
        and then all characters 'b' in the 2nd operation.
        So return 2 in this case
        """
        return 2 - (s == s[::-1]) - (s == "")