#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^=n
        return res
#print(Solution().singleNumber([2,2,1,1,3]))


# @lc code=end

