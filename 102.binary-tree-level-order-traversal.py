#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, level = [], [root]

        while root and level:
            res.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]
        return res
        

    def levelOrder_my(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        levelNodes,nextLevelNodes, levelVals, res = [],[],[],[]
        levelNodes.append(root)
        i = 0        
        while i < len(levelNodes):
            levelVals.append(levelNodes[i].val)
            if levelNodes[i].left:
                nextLevelNodes.append(levelNodes[i].left)
            if levelNodes[i].right:
                nextLevelNodes.append(levelNodes[i].right)                
            i +=1

            if  0 < i and i == len(levelNodes) and len(levelVals) > 0:
                res.append(levelVals.copy())
                levelNodes.clear()
                levelVals.clear()
                i = 0
                levelNodes = nextLevelNodes.copy()
                nextLevelNodes.clear()

        return res        


        
# @lc code=end

