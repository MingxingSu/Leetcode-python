#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    from typing import List
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:return 0
        lo, hi = 0, len(nums)-1

        while lo <=hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid +1
            elif nums[mid] > target:
                hi = mid -1
            else:
                return mid
            
            if target > nums[-1]: return len(nums)
            if target < nums[0]: return 0

        return lo

#print(Solution().searchInsert([1,3,5,6], 2))
        
# @lc code=end

