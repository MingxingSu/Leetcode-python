#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
#    from typing import List
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {}
        for i in range(len(s) - 9):
            tmp = s[i:i+10]
            dic[tmp] = dic.get(tmp, 0) + 1
            
        return [key for key,val in dic.items() if val > 1]


# @lc code=end

