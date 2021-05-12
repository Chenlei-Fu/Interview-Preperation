class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        #         if not nums or not nums[0]:
        #             return []

        #         d = collections.defaultdict(list)
        #         maxKey = -1
        #         for i in range(len(nums)):
        #             for j in range(len(nums[i])):
        #                 d[i+j].append(nums[i][j])
        #                 maxKey = max(maxKey, i + j)
        #         res = []
        #         for k in range(maxKey+1):
        #             res += d[k][::-1]
        #         return res

        res = []
        for i, r in enumerate(nums):
            for j, a in enumerate(r):
                if len(res) <= i + j:
                    res.append([])
                res[i + j].append(a)

        return [a for r in res for a in reversed(r)]