class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        I know 1 is ugly -> multiply 1 by 2, 3, 5 to get another ugly number
        the next number has to be the the smallest number among all the existing numbers multiplied by 2, 3,5 that isn't in the list already -> use three pointers to do so
        """
        if n <= 1:
            return n
        
        ugly = [1]
        p2 = p3 = p5 = 0
        for i in range(1, n):
            ugly.append(min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5))
            if ugly[i] == ugly[p2] * 2: p2 += 1
            if ugly[i] == ugly[p3] * 3: p3 += 1
            if ugly[i] == ugly[p5] * 5: p5 += 1
        return ugly[-1]
        
        