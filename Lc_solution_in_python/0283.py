from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for num in nums:
        #     if num == 0:
        #         nums.remove(num)
        #         nums.append(0)
        # return nums

        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[cur] = nums[cur], nums[i]
                cur += 1
        return nums