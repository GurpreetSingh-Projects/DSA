# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1
        max_p= 0

        while right < len(prices):

            if(prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                max_p= max(profit, max_p)
            else:
                left = right
            right+=1

        return max_p