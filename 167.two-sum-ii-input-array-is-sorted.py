#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    from typing import List
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:return []
        lo, hi = 0, len(numbers)-1
        while lo < hi:
            _sum = numbers[lo] + numbers[hi]
            if _sum > target:
                hi -=1
            elif _sum < target:
                lo +=1
            else:
                return [lo+1, hi+1]
        return []


#Solution().twoSum([2,7,11,15],9)      
# @lc code=end

