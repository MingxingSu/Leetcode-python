#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    from typing  import List
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1: return []
        if n ==1 : return ['()']

        res = []
        sub_res = self.generateParenthesis(n-1)
        
        for p in sub_res:
            wrap = '({0})'.format(p)
            if wrap not in res:
                res.append(wrap)
            
            mid = len(p) // 2

            inside = '{0}(){1}'.format(p[:mid], p[mid +1:])            
            if inside not in res:
                res.append(inside)            

            pre = '()' + p
            if pre not in res:
                res.append(pre)
            
            post = p  + '()'
            
            if post not in res:
                res.append(post)
        return res

print(len(Solution().generateParenthesis(4)))

        
# @lc code=end

