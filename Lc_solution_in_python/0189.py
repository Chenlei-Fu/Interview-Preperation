class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        
        method:
        reverse the first n - k elements
        reverse the rest of them
        reverse the entire array

        nums = [1,2,3,4,5,6,7], k = 3
        [4,3,2,1,5,6,7]
        [4,3,2,1,7,6,5]
        [5,6,7,1,2,3,4]
        """
        n = len(nums)
        k = k%n
        # method1: nums[:] = nums[n-k:] + nums[:n-k]
        
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1)
        return nums # for test
        
        
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
            
          
if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1,2,3,4,5,6,7], 3))
    