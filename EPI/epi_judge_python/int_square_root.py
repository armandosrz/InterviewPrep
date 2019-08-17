from test_framework import generic_test


def square_root(k):
    # as a fast way
    #return math.floor(math.sqrt(k))

    left, right = 0, k
    while left <= right:
        mid = left + (right-left)//2
        mid_square = mid * mid
        if mid_square <= k:
            left = mid +1
        else:
            right = mid -1

    return left-1        

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
