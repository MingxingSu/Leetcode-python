#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop()) #last element of list, and remove it
        rootIndex = inorder.index(root.val)

        root.right = self.buildTree(inorder[rootIndex+1:], postorder)#build right firstly
        root.left = self.buildTree(inorder[:rootIndex],postorder) #then build left, the order matters

        return root

        
# @lc code=end

