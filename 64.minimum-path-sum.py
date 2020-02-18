#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    from typing import List
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid),len(grid[0])
        if m==1 and n == 1: return grid[0][0]

        #define 2-d array: numpy.zeros(m,n)
        dp = [[0 for x in range(n)] for y in range(m)]

        #initialization
        dp[0][0] = grid[0][0]

        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]     
          
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) +  grid[i][j]                                        

        return dp[m-1][n-1]


# @lc code=end

