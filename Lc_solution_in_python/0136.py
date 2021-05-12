class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Method: xor all the bits
        a ^ a = 0
        a ^ 0 = a
        a ^ b ^ a = b
        """
        xor = 0
        for num in nums:
            xor ^= num
        return xor