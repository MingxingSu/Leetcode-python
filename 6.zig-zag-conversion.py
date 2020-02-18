#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows < 2: return s
        res = ''

        r, i = 0, 0

        for r in range(numRows):
            zig = 0
            step = 2*(numRows - r - 1)
            while i < len(s):
                zig +=1
                res +=s[i]

                if r in [0, numRows-1]:
                    i += 2*(numRows-1)
                else:
                    i += step if zig % 2 == 1 else 2*r
            i = r + 1

        return res

# @lc code=end

