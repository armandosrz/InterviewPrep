import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

'''
    Problem:
    Delete all duplicates in a sorted array. You are not allowed to 
    use library functions.

    Notes:
    - It is very important to comprehend the requiered inputs and 
     outputs before starting a problem.

    - Must of this test cases also only work if the solution is the 
      same as the best one in the books. 
'''

# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    visited = set()
    result = []
    for a in A:
        if a not in visited:
            result.append(a)
            visited.add(a)
    A = result
    return len(result), result

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    _, R = executor.run(functools.partial(delete_duplicates, A))
    return R


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
