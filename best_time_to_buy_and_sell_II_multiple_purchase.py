"""
 Best Time to Buy and Sell Stock II
 https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

 Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4
"""


class Stock:
    @staticmethod
    def max_profit(prices):
        if prices is None or len(prices) == 0:
            return -1
        minV = 0
        maxV = 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[maxV]:
                maxV = i
            elif prices[i] < prices[maxV]:
                current_profit = prices[maxV] - prices[minV]
                if current_profit > 0:
                    print("Buy on {} and sell on {} ".format(minV+1, maxV+1))
                    print("Current profit is {}".format(current_profit))
                    profit += current_profit
                minV = i
                maxV = minV
        print("Total profit is {}".format(profit))


if __name__ == "__main__":
    stock_prices = [7, 1, 5, 3, 6, 4]
    Stock().max_profit(stock_prices)
