#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        #dept first: begin from right kid
        self.flatten(root.right)
        self.flatten(root.left)

        #build list form bottom  to top.
        root.right = self.prev 
        root.left = None
        self.prev  = root

# @lc code=end

