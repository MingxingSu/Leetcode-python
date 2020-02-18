#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.03%)
# Likes:    1086
# Dislikes: 1526
# Total Accepted:    511.8K
# Total Submissions: 1.5M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1 if needle else  0

        le, lenn, lenhay = 0, len(needle), len(haystack)
        res = -1
        if lenhay == lenn:
            for i in range(lenn):
                if haystack[i] !=needle[i]:
                    return -1
            return 0

        while le < lenhay: 
            if needle[0] != haystack[le]:
                le +=1
            else:
                i = le + 1
                while i - le < lenn and i < lenhay and needle[i - le] == haystack[i] :
                    i +=1
                if i == lenn + le:
                    return le
                else:
                    le +=1
        return res
        
# @lc code=end

