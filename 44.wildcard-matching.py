#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def __init__(self):
        self.cache = {}

    def isMatch(self, s: str, p: str) -> bool:
        if (s,p) in self.cache:
            return self.cache[(s,p)]
        if not p:
            return not s      

        if s and (p[-1] == '?' or p[-1] == s[-1]) and self.isMatch(s[:-1], p[:-1]):  #Backtrack both:
            self.cache[(s,p)] = True
            return True
        if p[-1] == '*': 
            if s:
                if len(p)> 1 and (p[-2] in [s[-1],'?','*']) and self.isMatch(s, p[:-1]):#backtrack 1 step from pattern
                    self.cache[(s,p)] = True
                    return True       
                elif self.isMatch(s[:-1], p):#backtrack 1 step from input s
                    self.cache[(s,p)] = True 
                    return True
            else:
                if self.isMatch(s,p[:-1]):
                    self.cache[(s,p)] = True 
                    return True

        self.cache[(s,p)] = False
        return False 

#S= 'ho'
#P='ho**'
#print(Solution().isMatch(S,P))
# @lc code=end

