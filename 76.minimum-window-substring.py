#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        win,dic= '', {}
        tar_dic={}
        for c in t:
            tar_dic[c] = tar_dic.get(c,0)+1

        for i in range(len(s)):            
            if s[i] in t:
                dic[s[i]] = i

                if tar_dic[s[i]] > 0:
                    tar_dic[s[i]] -=1                

                if len(dic)==len(tar_dic):
                    if all(tar_dic):
                        vals = [v for v in dic.values()]
                        le, ri = min(vals), max(vals)
                        if not win or ri-le < len(win):#update min window
                            win = s[le:ri+1]
        return win
    
    def isSimilar(self,s,t):
        'ADEABOC' 'AABC'
        A:2, B:1, C:1
        A:1, A:0, B:0,C:0




S='aa'
T ='aa'
print(Solution().minWindow(S,T))

# @lc code=end

