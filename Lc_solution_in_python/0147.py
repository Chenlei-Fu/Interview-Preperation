# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        dummy = new ListNode(-1); //new starter of the sorted list (new head)
		cur = head; //the node will be inserted
		pre = dummy; //insert node between pre and pre.next
		next = null; //the next node will be inserted
        """
        if not head:
            return None
        
        dummy = ListNode(-1)
        cur, pre, next_ = head, dummy, None
        while cur:
            next_ = cur.next # store next for the next loop
            
            # check the existing new list
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            
            # insert new node to the new list
            cur.next = pre.next
            pre.next = cur
            pre = dummy
            cur = next_
        
        return dummy.next