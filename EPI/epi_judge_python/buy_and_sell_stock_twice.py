from test_framework import generic_test

'''
    Problem:
    Write a program that tells you the max profit you can make by buying and selling a stock
    twice. The second buy must be made on a date after the first sell.
'''

def buy_and_sell_stock_twice(prices):
    print(prices)
    # TODO - you fill in here.
    return 0.0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
