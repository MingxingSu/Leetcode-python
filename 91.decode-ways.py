#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:

    #w tells the number of ways
    #v tells the previous number of ways
    #d is the current digit
    #p is the previous digit
    def numDecodings(self, s: str) -> int:
        v, w, p = 0, int(s>''), ''
        for d in s:
            #dynamic programming
            v,w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d #update context for next iteration
        return w 


# @lc code=end

