#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    #step 1: dp[i][j]: when robot walk from top left to (i,j), how many possible paths? dp[m-1][n-1] is the final result we need


    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n: return 0
        if m ==1 or n == 1: return 1
        #define 2-d array: numpy.zeros(m,n)
        dp = [[0 for x in range(n)] for y in range(m)]

        #initialization
        dp[0][0] = 0

        for i in range(1,m):
            dp[i][0] = 1

        for j in range(1,n):
            dp[0][j] = 1           
          
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]                                    

        return dp[m-1][n-1]
    


        
# @lc code=end

