#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        s = ''
        while num > 0:
            s =capitals[(num-1)%26] + s
            num = (num-1) // 26
        return s
        
# @lc code=end

