#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    #trick: pick the bigger one and move it to the end of long list.
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -=1
        n -=1

        while m >= 0 and n >=0:            
            if nums1[m] < nums2[n]:
                nums1[m+n+1] = nums2[n]
                n -=1                
            else:
                nums1[m+n+1] = nums1[m]
                m -=1
        if n !=-1: # nums2 is still left
            nums1[:n+1] = nums2[:n+1]  

# @lc code=end

