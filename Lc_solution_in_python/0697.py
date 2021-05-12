class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq, first, res, degree = {}, {}, 0, 0
        
        for i, num in enumerate(nums):
            first.setdefault(num, i)
            freq[num] = freq.get(num, 0) + 1
            
            if freq[num] > degree: # update
                degree = freq[num]
                res = i - first[num] + 1
            elif freq[num] == degree:
                res = min(res, i - first[num] + 1)
        
        return res