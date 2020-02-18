#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:return None
        nodeA, nodeB = headA, headB

        # if either pointer hits the end, switch head and continue the second traversal, 
        # if not hit the end, just move on to next
        #O(m+n)
        while nodeA is not nodeB:
            nodeA = headB if nodeA is None else nodeA.next
            nodeB = headA if nodeB is None else nodeB.next          
    
        return nodeA

# @lc code=end

