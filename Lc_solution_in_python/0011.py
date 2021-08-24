from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        double pointers
        area = min(h[l], h[r]) * (r - l)
        """
        l, r, area = 0, len(height)-1, 0
        while l < r:
            h = min(height[l], height[r])
            area = max(area, h * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area