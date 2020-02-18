#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res ,nodes = [], [root]
        while len(nodes) > 0:
            res.append([node.val for node in nodes])
            nodes = [node for kid in nodes for node in [kid.left,kid.right] if node]
        return res[::-1]
        
# @lc code=end

