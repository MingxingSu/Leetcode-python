#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    from typing import List
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:return 0
        max_profit, min_price = 0, prices[0]
        i, end = 0, len(prices) - 1
        while i < end:
            while i < end and prices[i+1] < prices[i]:            
                i +=1
            min_price = prices[i]

            while i < end and prices[i+1] >  prices[i]:
                i +=1
            max_price = prices[i]
            
            max_profit += max_price - min_price
                
            i +=1
        
        return max_profit      
        
# @lc code=end

