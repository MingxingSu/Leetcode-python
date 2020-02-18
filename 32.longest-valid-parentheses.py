#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        maxans = 0
        if len(s) < 2: return maxans
        
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else: #')'
                if len(st) > 0:
                    if s[st[-1]] == '(':
                        st.pop()
                        maxans = max(maxans, i  - (st[-1] if st else -1))
                    else:
                        st.append(i)
                else:
                    st.append(i)
        return maxans


# @lc code=end

