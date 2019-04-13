"""
given a list of stock prices
prices = [12,11,15,3,10]
a function returns the maximum possible profit
7 (buying at 3 and selling at 10)

greedy algorithm:
iterate through the list of stock prices
while keeping track of the maximum profit
"""

def profit(stock_prices):

    min_stock_price = stock_prices[0]
    max_profit = 0

    for price in stock_prices:

        min_stock_price = min(min_stock_price,price)

        comparison_profit = price - min_stock_price

        max_profit = max(max_profit,comparison_profit)

    return max_profit


profit([23,12,3,10])