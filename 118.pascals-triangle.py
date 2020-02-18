#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    from typing import List
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1: return []        
        
        layer = [1]
        res = [layer]

        for i in range(2,numRows+1):
            newLayer = [1]*(len(layer) + 1)
            for j in range(1,len(newLayer)-1):
                newLayer[j] = layer[j] + layer[j-1]            
            res.append(newLayer)
            layer = newLayer                

        return res


#print(Solution().generate(5))



 
        
# @lc code=end

