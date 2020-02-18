#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return 0        
        nums.sort()
        minsum = nums[0]  + nums[1]  + nums[2]       
        for i in range(len(nums)-2):
            l , r = i +1, len(nums) -1
            while l < r:
                s = nums[i] + nums[l] + nums[r]                
                
                if s == target:
                    return s
                
                if abs(s - target) < abs(minsum - target):
                    minsum = s

                if s > target:
                    r -=1                
                elif s < target:
                    l +=1

        return minsum

# @lc code=end

