#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res


    def inorder(self, root:TreeNode, res:List[int]):
        if not root:
            return

        if root.left:
            self.inorder(root.left,res)

        res.append(root.val)

        if root.right:
            self.inorder(root.right,res)

        return res       

        
# @lc code=end

