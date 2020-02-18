#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, level = [], [root]
        counter = 0        
        while root and level:
            counter +=1
            flag = -1 if counter % 2 == 0 else 1        
            res.append([node.val for node in level][::flag])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res        
        
# @lc code=end

