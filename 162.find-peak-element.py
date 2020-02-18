#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    from typing import List
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:return -1
        if len(nums) == 1: return 0
        if len(nums) == 2: return 0 if nums[0] > nums[1] else 1

        le, ri = 0, len(nums)-1
        while le + 1 < ri:
            mid = (le + ri ) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid +1]:
                return mid
            if nums[mid] < nums[mid +1]:
                le = mid +1
            else:
                ri = mid -1

        return le if nums[le] > nums[ri] else ri

#Solution().findPeakElement([3,2,1])

        
# @lc code=end

