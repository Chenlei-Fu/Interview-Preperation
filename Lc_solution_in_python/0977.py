class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        res, p = [0] * n, n-1
        for p in range(n-1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                res[p] = nums[r]**2
                r -= 1
            else:
                res[p] = nums[l] ** 2
                l += 1
        return res