#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res,base = '',ord('0')
        l = max(len(a),len(b))
        a, b = a.rjust(l,'0'), b.rjust(l,'0')

        l -=1
        sur = 0        
        while l >=0:

            sum = sur + ord(a[l])- base  +  ord(b[l])- base
            if sum > 1:
                sur = 1
                sum %=2
            else:
                sur = 0

            res = chr(sum+base) + res
            l -=1

        return '1' + res if sur else res

#Solution().addBinary('1111','1111')            



# @lc code=end

