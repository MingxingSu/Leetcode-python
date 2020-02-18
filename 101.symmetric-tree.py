#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSym(root,root)

    def isSym(self, L, R):
        if not L and not R:return True
        if L and R and L.val == R.val:
            return self.isSym(L.left, R.right) and self.isSym(L.right, R.left)
        return False

# @lc code=end

