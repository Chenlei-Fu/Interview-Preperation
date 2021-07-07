class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x+1
        while l < r:
            mid = l + (r-l)//2
            if mid * mid > x:
                r = mid
            else:
                l = mid + 1
        return l-1 # since l * l > x