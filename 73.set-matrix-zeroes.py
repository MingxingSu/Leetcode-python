#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (41.02%)
# Likes:    1341
# Dislikes: 232
# Total Accepted:    245.5K
# Total Submissions: 596.3K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0: return
        m, n = len(matrix), len(matrix[0])
        zeros_x, zeros_y = [],[]

        #mark zero element's x and y axis
        for i in range(m):            
            for j  in range(n):
                if matrix[i][j] == 0:
                    if i not in zeros_x:
                        zeros_x.append(i)
                    if j not in zeros_y:
                        zeros_y.append(j)
        #set to zeros
        for x in zeros_x:
            for j in range(n):
                matrix[x][j] = 0
        for y in zeros_y:
            for i in range(m):
                matrix[i][y] = 0
        
# @lc code=end

