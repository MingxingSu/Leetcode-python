#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    from typing import List
    def maximalRectangle(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
                
        n = len(grid[0])
        height = [0]* (n + 1)
        ans = 0
        
        for row in grid:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0

            stack = [-1]
            for i in range(n+1):                    
                while height[i] < height[stack[-1] if stack else 0]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h*w)

                stack.append(i)

        return ans


# @lc code=end

