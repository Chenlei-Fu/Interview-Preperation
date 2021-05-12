class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        """
        one pass
        """
        local_max, global_max = 0, 0
        nums.append(-sys.maxsize)
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                local_max += nums[i]
            else:
                local_max += nums[i]
                global_max = max(local_max, global_max)
                local_max = 0
            # print(local_max, global_max)
        return global_max
    
    
    