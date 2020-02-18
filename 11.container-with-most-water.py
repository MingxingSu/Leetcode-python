#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    from typing import List
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2: return 0
        maxa,area = 0,0
        le, ri= 0, len(height) -1

        while le != ri :
            
            if height[le] > height[ri]:
                area = height[ri]* (ri - le)
                ri -=1
            else:
                area = height[le]* (ri - le)
                le +=1
            maxa = max(maxa, area)
        return maxa


        