#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ones = []
        if len(nums)==0: return
        lo, hi = 0, len(nums) - 1
        zero, one, two = 0, 0,0
        while lo <= hi:
            if nums[lo] == 0:
                zero +=1
            elif nums[lo] == 1:
                one +=1
            else:
                two +=1
            lo +=1

        i = 0
        while i < zero:
            nums[i] = 0
            i +=1
        i = 0
        while i < one:
            nums[i+zero] = 1
            i +=1
        i = 0
        while i < two:
            nums[i+zero+one] = 2
            i +=1

        
# @lc code=end

