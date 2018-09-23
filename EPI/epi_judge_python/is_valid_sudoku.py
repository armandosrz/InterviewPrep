from test_framework import generic_test

'''
    This particular problem focuses on implementing
    clean code.
'''


import math
# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    # check Horizontal
    for row in partial_assignment:
        if not all_unique(row):
            return False
    
    # check vertical by doing a transpose 
    for row in zip(*partial_assignment):
        if not all_unique(row):
            return False
    
    size = int(math.sqrt(len(partial_assignment)))

    # Check all subsections
    for a in range(size):
        for b in range(size):
            target = [
                      partial_assignment[i][j]
                      for i in range(a * size, size * (a+1))
                      for j in range(b*size, size * (b+1))
                     ]
            if not all_unique(target):
                return False


    return True


def all_unique(A):
    seen = set()
    A = list(filter(lambda x: x!=0, A))
    return not any(i in seen or seen.add(i) for i in A)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
