# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Solution 1

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


# Solution 2

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_p, l,r = 0, 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                max_p = max(max_p, prices[r] - prices[l])
            else:
                l = r

            r+=1
        return max_p