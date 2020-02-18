#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.75%)
# Likes:    5333
# Dislikes: 216
# Total Accepted:    665K
# Total Submissions: 1.5M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len([n for n in nums if n < 0]) == len(nums):
            return max(nums)

        tempSum,maxSum = 0, 0
        for i in range(len(nums)):   
            tempSum +=nums[i]              
            if tempSum > maxSum:
                maxSum = tempSum                
            elif tempSum < 0:
                tempSum = 0
                maxSum = maxSum if maxSum > 0 else 0 #Important: make sure the maxSum already got before tempSum < 0
            

        return maxSum

# @lc code=end

