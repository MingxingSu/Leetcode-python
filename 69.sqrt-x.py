#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:return x
        lo, hi = 0,x // 2

        while lo <= hi:
            mid = (lo + hi ) // 2
            sq = mid*mid
            if sq > x:
                hi = mid -1
            elif sq < x:
                lo = mid +1
            else:
                return mid
        return lo-1
    
#print(Solution().mySqrt(4))

        
# @lc code=end

