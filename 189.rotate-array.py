#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        r = nums[-k:] + nums[0:-k]
        for i in range(len(r)):
            nums[i] = r[i]        


             
    def rotate_v2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = [0] * len(nums)
        for i in range(len(nums)):
            a[(i+k)%len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = a[i]        
        #nums = nums[-k:] + nums[:-k]
        
# @lc code=end

