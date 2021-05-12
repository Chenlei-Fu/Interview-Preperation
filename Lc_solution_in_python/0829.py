class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # Sum of Arithmetic Sequence
        # x + (x+1) + (x + 2) + ... + (x + k-1) = N
        # kx + (k) *(k-1)/2 = N
        # kx = N - k * (k-1)/2
        # try every k from 1 until N - k * (k-1)/2 > 0

        i, ans = 1, 0
        while N > i * (i - 1) // 2:
            if (N - i * (i - 1) // 2) % i == 0:
                ans += 1
            i += 1
        return ans