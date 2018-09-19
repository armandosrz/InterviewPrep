from test_framework import generic_test


'''
    Problem:
    Write a program that determines the max amount of profit you can
    make by buying/selling stocks in different dates.

    Input:
    - An array in which has the values for each day. 

    Notes:
    - Implement using a greedy approach. Keep track of both the max profit and the lowest
      found element.
    
    Solution:
    - Perfomance: O(n)
    - Space: O(1)
'''

def buy_and_sell_stock_once(prices):
    low, profit = float('inf'), 0.0

    for price in prices:
        if price - low > profit:
            profit = price - low
        if price < low:
            low = price

    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
