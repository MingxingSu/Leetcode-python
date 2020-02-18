#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        st = [str.lower(c) for c in s if c.isalnum()]        
        return st == st[::-1]
        
# @lc code=end

