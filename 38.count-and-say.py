#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n== 1: return '1'
        pre = self.countAndSay(n-1)
        s, i = '', 0
        while i <= len(pre)-1:
            count =1
            while i < len(pre)-1 and pre[i] == pre[i+1]:
                count +=1
                i +=1
            s +=str(count)+pre[i]
            i +=1
        return s        
# @lc code=end

