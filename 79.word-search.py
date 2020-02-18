#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    from typing import List
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j,word):
                    return True
        return False

    def dfs(self, A:List[List[str]],i:int, j:int, word:str) ->bool:
        if len(word) == 0:
            return True
        if i < 0 or i >=len(A) or j < 0 or j >=len(A[0]) or word[0] !=A[i][j]:
            return False
        tmp = A[i][j] # first char of word found.
        A[i][j] = '#' # avoid visit it again

        #left, right, up, down
        res =  self.dfs(A,i, j-1, word[1:]) or  self.dfs(A,i, j+1, word[1:]) or \
             self.dfs(A,i-1, j, word[1:])  or self.dfs(A,i+1, j, word[1:]) 

        A[i][j] = tmp #recover it

        return res
        
# @lc code=end

