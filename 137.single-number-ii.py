#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    from typing import List
    def singleNumber(self, nums):
        one, two = 0, 0
        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            one, two = one & ~three, two & ~three
        return one

    def singleNumber2(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n,0)+1
        for k,v in dic.items():
            if v == 1:
                return k


#print(Solution().singleNumber([2,2,3,2]))
# @lc code=end

