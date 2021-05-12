class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        """
        greedy algorithm
        """
        A = sorted(A)
        take = collections.defaultdict(list) # 用list是为了考虑数字重复的情况
        for b in sorted(B)[::-1]:
            if b < A[-1]:
                take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]