# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2, dummy = l1, l2, ListNode(-1)
        cur, carry = dummy, 0
        while p1 or p2 or carry:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            s = p1_val + p2_val + carry
            carry, out = divmod(p1_val + p2_val + carry, 10)
            cur.next = ListNode(out)
            cur = cur.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            
        return dummy.next
        