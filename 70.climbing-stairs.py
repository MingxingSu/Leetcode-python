#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    #step 1: define meaning of dp[i]: count of steps taken to reach i stair
    #step 2: formaula: dp[n] = dp[n-1] + dp[n-2]
    #step 3: initial values
    def climbStairs(self, n: int) -> int:
        if n <=2: return n
        dp = [0]*(n+1)
        dp[0], dp[1] , dp[2]  = 0, 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# @lc code=end

