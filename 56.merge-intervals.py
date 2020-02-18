#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (36.83%)
# Likes:    2694
# Dislikes: 211
# Total Accepted:    431.5K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
class Solution:


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        A = sorted(intervals, key=lambda  x: x.start)
        intervals[0].start
        i = 0
        while i< len(A)-1:
            if A[i+1][0] <= A[i][1]:
                if A[i][1]  <= A[i+1][1]:
                    A[i+1][0] = A[i][0]
                    del A[i]
                    i -=1
                else:
                    del A[i+1]
                    i -=1
            i += 1

        return A 


# @lc code=end

