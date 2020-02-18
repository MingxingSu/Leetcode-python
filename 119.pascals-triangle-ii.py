#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    from typing import List    
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 1: return [1]        
        
        layer = [1]
        for i in range(1,rowIndex+1):
            newLayer = [1]*(len(layer) + 1)
            for j in range(1,len(newLayer)-1):
                newLayer[j] = layer[j] + layer[j-1]            
            layer = newLayer

        return layer


#print(Solution().getRow(3))
        
# @lc code=end

