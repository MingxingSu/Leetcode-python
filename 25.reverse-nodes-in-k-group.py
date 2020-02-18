#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (38.14%)
# Likes:    1445
# Dislikes: 290
# Total Accepted:    211.8K
# Total Submissions: 554K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #Use a dummy head, and

    #l, r : define reversing range

    #pre, cur : used in reversing, standard reverse linked linked list method

    #jump : used to connect last node in previous k-group to first node in following k-group
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                r = r.next
                count +=1
            
            if count == k:
                pre, cur = r, l
                
                for _ in range(k):
                    cur.next, pre, cur = pre, cur, cur.next #standard reverse
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else: 
                return dummy.next
# @lc code=end

