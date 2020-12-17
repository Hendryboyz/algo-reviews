'''
LeetCode 121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a
given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm
to find the maximum profit.

Note that you cannot sell a stock before you buy one.
'''
def max_profit(prices: [int]) -> int:
  max_profit = 0
  buy_time = 0
  for time in range(len(prices)):
    profit = prices[time] - prices[buy_time] if time > buy_time else 0
    if profit > max_profit:
      max_profit = profit
    if prices[time] < prices[buy_time]:
      buy_time = time 
  return max_profit
