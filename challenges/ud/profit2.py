# Python 3.7.2
# A list of stock prices for a day
# Write a function to return the maximum profit 
# (buy at the lowest price and later sell at the highest price)

def profit2(stock_prices):

    # Edge Case
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices!')

    # Minimum price at first price
    min_stock_price = stock_prices[0]

    # Initial max profit
    max_profit = stock_prices[1] - stock_prices[0]

    # Skip the first index price
    for price in stock_prices[1:]:
        # Check the current price against the minimum for a profit
        comparison_profit = price - min_stock_price

        # Compare against the max_profit so far
        max_profit = max(max_profit,comparison_profit)

        # Check to set the lowest stock price so far
        min_stock_price = min(min_stock_price, price)

    return max_profit


"""

Test sample
profit([10,12,14,12,13,11,8,7,6,13,23,45,11,10])

"""