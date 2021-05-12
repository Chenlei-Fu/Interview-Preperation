class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        """
        Result is the integer ceil of fraction diff / limit.
        In math it equals to (diff + limit - 1) / limit
        """
        return int((abs(sum(nums) - goal) + limit - 1) / limit)