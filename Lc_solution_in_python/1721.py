# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p = head
        for i in range(k-1):
            p = p.next
        fast, slow = p.next, head
        while fast != None:
            fast = fast.next
            slow = slow.next
        p.val, slow.val = slow.val, p.val
        return head
            