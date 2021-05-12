from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        """
        method1: DP
        """
        dp, res = [1] * len(nums), 0
        for i in range(len(nums)):
            localMax = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    localMax = max(localMax, dp[j] + 1)
            dp[i] = localMax
            res = max(res, dp[i])
        return res

        """
        method2: binary search
        try to insert the next number to the dp array (generate new array)
        """
        dp = []
        for num in nums:
            idx = bisect_left(dp, num)
            if idx == len(dp): # no value smaller than num
                dp.append(num)
            else:
                dp[idx] = num
        return len(dp)

        """
        method3: binary search
        """
        n = len(nums)
        dp, size = [0] * n, 0
        for num in nums:
            # binary search for the right most elem smaller than num
            l, r = 0, size
            while l < r:
                mid = l + (r - l) // 2
                if dp[mid] < num:
                    l = mid + 1
                else:
                    r = mid  
            dp[l] = num
            if (l == size): size += 1
        return size