# 3.7.2
'''
You've been given a list of historical stock prices for a single day for CompanyA stock. The index of the list represents the timestamp, so the element at index of 0 is the initial price of the stock, the element at index 1 is the next recorded price of the stock for that day, etc. Your task is to write a function that will return the maximum profit possible from the purchase and sale of a single share of CompanyA stock on that day. Keep in mind to try to make this as efficient as possible.

stock_prices = [12,11,15,3,10]
'''

def profit1(stock_prices):

    # start minimum price marker at first price
    min_stock_price = stock_prices[0]

    # start off with a profit of zero
    max_profit = 0

    for price in stock_prices:

        # check the lowest price so far
        min_stock_price = min(min_stock_price,price)

        # check the current price against the min stock price for a profit
        comparison_profit = price - min_stock_price

        # compare against the max profit so far
        max_profit = max(max_profit, comparison_profit)

    return max_profit