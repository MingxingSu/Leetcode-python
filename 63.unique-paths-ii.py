#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    from typing import List
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        if len(obstacleGrid) ==1 and len(obstacleGrid[0]) == 1: 
            return 0 if obstacleGrid[0][0] else 1
                
        m, n = len(obstacleGrid),len(obstacleGrid[0])

        #define 2-d array: numpy.zeros(m,n)
        dp = [[0 for y in range(n)] for x in range(m)]

        #initialization

        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] if not obstacleGrid[i][0] else 0
            
        for j in range(1,n):
             dp[0][j] = dp[0][j-1] if not obstacleGrid[0][j] else 0        
          
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if not obstacleGrid[i][j] else 0

        return dp[m-1][n-1]

print(Solution().uniquePathsWithObstacles([[0,1]]))

# @lc code=end

