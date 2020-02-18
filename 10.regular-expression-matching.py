# @lc code=start
class Solution:
    # * -- zero or more
    # . -- any char
    cache = {}
    def isMatch(self, s: str, p: str) -> bool:
        if (s,p) in self.cache:
            return self.cache[(s,p)]
        if not p:
            return not s

        #Backtrack both: when pattern ends with dot, or their ends match
        if s and (p[-1] == '.' or p[-1] == s[-1]) and self.isMatch(s[:-1], p[:-1]):
            self.cache[(s,p)] = True
            return True
        if p[-1] == '*': 
            #Backtrack input: when input's end matches with pattern
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[0:-1],p):
                self.cache[(s,p)] = True #p[-1] matches s[-1]
                return True
            #Backtrack pattern
            if self.isMatch(s, p[:-2]): # the last 2 chars of pattern can be ignored as a new pattern
                self.cache[(s,p)] = True
                return True                

        self.cache[(s,p)] = False
        return False
        
# @lc code=end

