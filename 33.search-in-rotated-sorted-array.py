#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (33.23%)
# Likes:    3093
# Dislikes: 368
# Total Accepted:    500.6K
# Total Submissions: 1.5M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        le, ri = 0, len(nums)-1
        
        while le <= ri:
            mid = (le + ri ) // 2            
            if nums[mid] == target:
                return mid
                                           
            #left 
            if nums[le] <= nums[mid]:
                if nums[le] <= target <=nums[mid]:
                   ri = mid -1
                else:
                    le = mid + 1
            else: 
                if nums[mid] <= target <=nums[ri]:
                    le = mid + 1
                else:
                    ri = mid - 1
        return -1
# @lc code=end

