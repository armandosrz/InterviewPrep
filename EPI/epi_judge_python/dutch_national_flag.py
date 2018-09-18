import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

'''
    Problem:

    Write a program that takes an array A and index i (pivot) and those the following:
    - All elements smaller than pivot should go first
    - follow by elements equal to pivot
    - and ending by elements bigger than pivot

    Notes: elements in subpartition do not need to be sorted as long as the 
           ordering is correct. This is a modification of a quick sort algorithm. 

'''

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        # when smaller, swap element into smaller group
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller +=1
            equal +=1
        # if equal, keep moving
        elif A[equal] == pivot:
            equal+=1
        # when larger, move to end group.
        # do not update equal since element is unknown
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    return A
            
    # Brute Force, solution has O(n) of extra space.
    '''
    target = A[pivot_index]
    left = []
    center = []
    rigth = []
    for a in A:
        if a < target:
            left.append(a)
        elif a == target:
            center.append(a)
        else:
            rigth.append(a)
    return left + center + rigth
    '''


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    A = executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))
    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
