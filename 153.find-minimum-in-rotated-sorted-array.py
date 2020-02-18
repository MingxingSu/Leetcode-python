#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    from typing import List
    def findMin(self, nums: List[int]) -> int:
        if not nums:return -1
        if len(nums) == 1: return nums[0]

        le, ri = 0, len(nums)-1
        while le < ri:
            mid = (le + ri ) // 2
            if mid > 0 and mid +1 <= ri:
                if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                    return nums[mid]
                else:
                    return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))
            else:
                return min(nums[mid], nums[mid+1])
        return nums[le]

#print(Solution().findMin([5,4]))
#print(Solution().findMin([3,4,5,1,2]))


        
# @lc code=end

