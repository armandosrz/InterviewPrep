from test_framework import generic_test


def number_of_ways(n, m):
    def compute(x, y):
        if x == y == 0:
            return 1
        if squares[x][y] != 0:
            return squares[x][y]
        
        left = compute(x-1, y) if x != 0 else 0
        top = compute(x, y-1) if y != 0 else 0
        squares[x][y] = left + top
        
        return left + top
    
    squares = [[0] * m for _ in range(n)]
    return compute(n-1, m-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
