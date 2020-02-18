#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:    
    def __init__(self):
        self.dt = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}        
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return [] 

        res = []
        self.dfs(res,digits,'')
        return res
    
    def dfs(self, res:List[str], digits:str,path:str):        
        if not digits:
            res.append(path)
            return
        
        for c in self.dt[digits[0]]:
            path += c
            self.dfs(res,digits[1:], path)
            path = path[0:-1]

        
# @lc code=end

