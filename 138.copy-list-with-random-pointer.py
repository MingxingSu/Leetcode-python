#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy, cur, newHead = Node(0, None), head, None
        dummy.next = newHead
        cache ={}

        while cur:
            newHead = Node(cur.val, None)
            if cur.val not in cache:
                cache[cur.val]= (newHead, cur.random)
            newHead.next = newHead
            cur = cur.next        

        tmp = newHead
        while tmp:
            tmp.random = cache[cache[tmp.val][1].val][0]
            tmp = tmp.next
        
        return dummy.next

        
        
# @lc code=end

