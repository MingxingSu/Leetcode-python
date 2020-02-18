#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeights(root,res):
            if not root: return 0            
            l = getHeights(root.left,res)
            r = getHeights(root.right,res)
            res[root] = max(l, r) + 1
            return max(l, r) + 1

        if not root: return True
        res = {}
        getHeights(root,res)
        nodes = [root]
        while len(nodes) > 0:        
            for n in nodes:
                lh = res[n.left] if n.left else 0
                rh = res[n.right] if n.right else 0
                if lh-rh > 1 or rh - lh > 1:
                    return False
            nodes = [node for kid in nodes for node in [kid.left, kid.right] if node]

        return True


    def isBalanced_v1(self, root: TreeNode) -> bool:
        if not root: return True

        def maxDept(root):
            if not root: return 0
            return max(maxDept(root.left),maxDept(root.right))+1
        
        return self.isBalanced(root.left) and self.isBalanced(root.right) and -1<= maxDept(root.left) -maxDept(root.right) <=1

        
# @lc code=end

