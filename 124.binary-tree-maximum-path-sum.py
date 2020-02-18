#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:        
        def maxend(root):
            if not root: 
                return 0
            le_sum = maxend(root.left)
            ri_sum = maxend(root.right)
            
            #update global max sum
            self.max = max(self.max, le_sum + root.val + ri_sum)
            
            return max(0, max(le_sum,ri_sum) + root.val)

        self.max = -1*2**32
        maxend(root)
        return self.max
                
# @lc code=end

