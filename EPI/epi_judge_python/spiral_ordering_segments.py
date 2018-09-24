from test_framework import generic_test


'''
    Problem:
    Given an square matrix, provide a list of elements in spiral order.

    Notes:
    The first thing to note is what means to go a certian direction. Assuming
    row = i and col = j and starting at (0,0):
    - right: j + 1
    - down: i + 1
    - left: j - 1
    - up: i - 1

    Once that define, then we need to know when we change in direction. We will
    change when a certain element goes out of bounds or a arrive to an element
    that has been visited. In order to not increase more memory, and under 
    the assumption that all members of the array are positive we 
    can mark this as a `-1`.

    With this then we can come up with the following implementation:
'''

def matrix_in_spiral_order(square_matrix):
    if not square_matrix:
        return []
    
    def isBoudary(i, j):
        if (i >= n or i < 0) or (j >= n or j < 0):
            return True
        if square_matrix[i][j] == -1:
            return True
        else:
            False

   
    n = len(square_matrix)
    out = []
    i, j = 0, 0

    out.append(square_matrix[i][j])
    direction = 'r'
    square_matrix[i][j] = -1

    count = 1
    while count < n*n:
        if direction == 'r':
            if not isBoudary(i, j+1):
                j += 1
                out.append(square_matrix[i][j])
                square_matrix[i][j] = -1
                count +=1
            else:
                direction = 'd'
        
        if direction == 'd':
            if not isBoudary(i+1, j):
                i += 1
                out.append(square_matrix[i][j])
                square_matrix[i][j] = -1
                count +=1
            else:
                direction = 'l'
        
        if direction == 'l':
            if not isBoudary(i, j-1):
                j -= 1
                out.append(square_matrix[i][j])
                square_matrix[i][j] = -1
                count +=1
            else:
                direction = 'u'
        
        if direction == 'u':
            if not isBoudary(i-1, j):
                i -= 1
                out.append(square_matrix[i][j])
                square_matrix[i][j] = -1
                count +=1
            else:
                direction = 'r'
    
    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
