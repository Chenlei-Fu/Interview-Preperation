class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 0
        for i in range(1, len(nums)):
            if nums[ptr] != nums[i]:
                ptr += 1
                nums[ptr] = nums[i]
        return ptr + 1