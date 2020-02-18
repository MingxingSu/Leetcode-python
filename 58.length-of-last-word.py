#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        count = 0
        s = s.strip()        
        i = len(s)-1
        while i >=0 and s[i] !=' ':
            count +=1
            i -=1
        return count


    def lengthOfLastWord_v2(self, s: str) -> int:
        if not s: return 0
        s = s.strip()
        if not len(s): return 0
        return len(s.split()[-1])
        
# @lc code=end

