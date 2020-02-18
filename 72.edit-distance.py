#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:return len(word2)
        if not word2:return len(word1)        

        #step 1 definition=> i: index of word1, j: index of word2, 
        #dp[i][j]: min distance word1->word2
        m , n = len(word1), len(word2)                
        dp = [[0]*(n+1) for _ in range(m+1)]

        #step 2 => initials        
        for i in range(m+1): 
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j
        
        #step 2 =>formula: dp[i][j], dp[i-1][j], dp[i][j-1]        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] ==word2[j-1]:#pre char matches, no action needed
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1]) + 1              

        return dp[-1][-1]
        
# @lc code=end

