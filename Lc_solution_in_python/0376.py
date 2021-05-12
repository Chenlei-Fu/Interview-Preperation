class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        up[i] -> keep the max length at index i with up state
        down[i] -> keep the max length at index i with down state
        """
        length = len(nums)
        if length == 0:
            return 0
        
        up, down = [0] * (length), [0] * length
        up[0], down[0] = 1, 1
        for i in range(1, length):
            if nums[i] > nums[i-1]: # up
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
                
        return max(down[length-1], up[length-1])