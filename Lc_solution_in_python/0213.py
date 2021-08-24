class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        return max(self.helper(nums, 0, n-2), self.helper(nums, 1, n-1))
    
    def helper(self, nums, begin, end):
        pre2, pre1 = 0, 0
        for i in range(begin, end + 1):
            cur = max(pre2 + nums[i], pre1)
            pre2 = pre1
            pre1 = cur
        return cur