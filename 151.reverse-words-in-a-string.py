#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ''

        return ' '.join([x for x in s.strip().split() if x][::-1])
        
# @lc code=end

