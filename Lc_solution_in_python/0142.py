# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        slower, faster = head, head
        while faster.next and faster.next.next:
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                tmp = head
                while tmp != slower:
                    tmp = tmp.next
                    slower = slower.next
                return tmp
        return None
        
        