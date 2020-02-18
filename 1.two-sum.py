#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.51%)
# Likes:    11796
# Dislikes: 406
# Total Accepted:    2.1M
# Total Submissions: 4.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

import sys
sys.path = r'/home/jessiesofie0720/LeetcodesProjects'

class Solution:
    def twoSum(self, nums, target):
        dt ={}
        for i in range(len(nums)):
            if target- nums[i] in dt:
                return [dt[target- nums[i]], i]
            else:
                dt[nums[i]] = i          
        return []

if __name__ == "__main__":
    Solution().twoSum([1,2,4], 3)

