# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        如果ha先结束，让他走hb的路
        否则TLE
        """
        ha, hb = headA, headB
        while ha != hb:
            ha = ha.next if ha != None else headB 
            hb = hb.next if hb != None else headA
        return ha
    