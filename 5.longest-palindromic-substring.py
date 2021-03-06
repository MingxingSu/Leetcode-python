#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res =''
        for i in range(len(s)):
            #odd like 'aba'
            temp = self.helper(s, i, i)
            if len(temp) > len(res):
                res = temp
          
            #even case, like 'abba' 
            temp = self.helper(s, i, i+1)
            if len(temp) > len(res):
                res = temp
        return res

    def helper(self,s:str, l:int, r:int) -> str:
        #extend to both sides
        while l >=0 and r < len(s) and s[l] == s[r]:
            l -=1
            r +=1
        return s[l+1:r]

