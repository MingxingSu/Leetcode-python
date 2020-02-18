#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    from typing import List
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in sorted(nums):
            res += [subset + [n] for subset in res]
        return res


    def subsets_v1(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
                    


#print(Solution().subsets([2,1,3]))

        
# @lc code=end

