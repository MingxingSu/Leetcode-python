#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:return []
        pre = 1

        i = len(digits) -1

        while i >=0:
            _sum = pre + digits[i]

            if _sum > 9:
                pre = 1
                digits[i] = 0
            else:
                pre = 0
                digits[i] = _sum
            i -=1
        if pre == 1:
            return ['1']+ digits
        else:
            return digits
        
# @lc code=end

