#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    from typing import List
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        dt = {}
        for n in nums:
            if n in dt:
                dt[n] +=1
            else:
                dt[n] = 1
        for kv in dt.items():
            if kv[1] > mid:
                return kv[0]


    #other approach:
    def majorityElement_v2(self, nums: List[int]) -> int:
        return sorted(num)[len(num)/2]
        
# @lc code=end

