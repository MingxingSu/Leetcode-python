#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (57.82%)
# Likes:    2572
# Dislikes: 84
# Total Accepted:    454K
# Total Submissions: 781.5K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start

class Solution:
    from typing import List

    res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        selected = []
        self.res.clear()
        self.helper(selected, nums,0)
        return self.res


    def helper(self, selected:List[int], nums:List[int], pos:int):        
        #exit condition
        if(pos == len(nums)):
            self.res.append(selected.copy())
            return

        #iterate the pool
        for n in nums:

            #skip already selected elements
            if n in selected:
                continue
            selected.append(n)

            #select next element with dept first searching
            self.helper(selected, nums, pos + 1)

            del selected[-1] # backtrack to previous step     


    # DFS
    def permute_dfs(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in xrange(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
# @lc code=end

