# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = self.getLength(root)
        size, mod = n // k, n % k
        prev, cur = None, root
        res = [size + 1] * mod + [size] * (k - mod)
        print(res, size, mod)
        for i, boxSize in enumerate(res):
            if prev:
                prev.next = None
            res[i] = cur
            for _ in range(boxSize):
                prev, cur = cur, cur.next
        return res

    def getLength(self, root):
        res, cur = 0, root
        while cur:
            cur = cur.next
            res += 1
        return res