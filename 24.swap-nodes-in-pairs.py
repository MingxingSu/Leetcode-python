#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (46.63%)
# Likes:    1454
# Dislikes: 129
# Total Accepted:    365.9K
# Total Submissions: 782.8K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Hi 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



#Here, pre is the previous node. Since the head doesn’t have a previous node, 
# I just use self instead.  a is the current node and b is the next node.
# To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next
# we need to change those three references. 
# Instead of thinking about in what order I change them, I just change all three at once

 
class Solution:
    # pre->a -> b ->b.next ==> pre -> b -> a - > b.next
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next            
            pre.next,b.next, a.next = b ,a, b.next
            pre = a

        return self.next
        
# @lc code=end

