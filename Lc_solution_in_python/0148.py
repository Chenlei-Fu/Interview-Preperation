# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: # important!!
            return head
        
        slower = faster = head
        while faster.next and faster.next.next:
            slower = slower.next
            faster = faster.next.next 
        mid = slower.next
        slower.next = None
        return self.merge(self.sortList(head), self.sortList(mid))
    
    def merge(self, l, r):
        dummy = cur = ListNode(-1)
        while l and r:
            if l.val < r.val:
                cur.next = ListNode(l.val)
                l = l.next
            else:
                cur.next = ListNode(r.val)
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next