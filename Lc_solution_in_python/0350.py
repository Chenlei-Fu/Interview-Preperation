from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        method 1
        """
        # from collections import Counter
        # return (Counter(nums1) & Counter(nums2)).elements()


        """
        method2: sort and two pointer
        """
        #
        # p1, p2, sorted_nums1, sorted_nums2, res = 0, 0, sorted(nums1), sorted(nums2), []
        # while p1 < len(sorted_nums1) and p2 < len(sorted_nums2):
        #     if sorted_nums1[p1] < sorted_nums2[p2]:
        #         p1 += 1
        #     elif sorted_nums1[p1] > sorted_nums2[p2]:
        #         p2 += 1
        #     else:
        #         res.append(sorted_nums2[p2])
        #         p1 += 1
        #         p2 += 1
        # return res

        """
        method 3:
        dictionary
        """
        freq, res = {}, []
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1
        for num in nums2:
            if num in freq and freq[num] > 0:
                res.append(num)
                freq[num] -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(s.intersect(nums1, nums2))