from test_framework import generic_test

'''
    Problem:
    Write a program that takes an array of digits that represent a non-negative
    integer. Write a program that will update the quantity by one.
    Ex. <1,2,9> will return <1,3,0>

    Notes:
    - Brute force approach would be to join as a string -> convert to int -> add one
      -> back into a list.
    If we try to do in place:
    - Need to perform carry over operation when a 9 is encounter on the right-most element.
    - Edge case will be if all elements are 9's, we will create a new array with a 1 follow
      by all zeros.

    Algorithm:
    We start at the end of the array, we loop while i is more than 0 where i is len(A) - 1
    - If a number is 9 set to 0 and check neighbor (if neighbor is also 9, decrement i, else increase neighbor by one and return)

    Performance:
    - O(n)
    - Space: O(1) common and 0(n) worst case
'''

def plus_one(A):
    i = len(A) -1
 
    while i > 0:
        if A[i] == 9:
            A[i] = 0
            if A[i-1] < 9:
                A[i-1] += 1
                return A
            i -= 1
        else:
            A[i] += 1
            return A
    
    if A[0] == 9:
        return [1] + [0] * len(A)
    
    A[0] += 1
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
