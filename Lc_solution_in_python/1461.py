class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        """
        sliding window
        note that the number of distinct sub-strings should be exactly 2^k.
        time: O(k * n)
        space: O(2^k * k)
        """
        seen = set()
        for i in range(len(s) - k + 1):
            seen.add(s[i: i+k])
        return len(seen) == (1<<k)