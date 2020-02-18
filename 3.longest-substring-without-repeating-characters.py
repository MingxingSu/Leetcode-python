#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        maxsub = 0
        sub = ''

        for i in range(len(s)):
            if s[i] in sub:
                dup = sub.index(s[i])
                sub = sub[dup+1:]
            sub +=s[i]
            maxsub = max(maxsub, len(sub))

        return maxsub
        
# @lc code=end

