from test_framework import generic_test

'''
    Problem:
    Apply permutation to A.
    Where perm is an array in which element the element at i, should be 
    move to P[i]

    Notes:
    - This is a simple problem if the result is store in a new array.
    - If we try to accomodate in place, we need to know if a specific element
      has been moved already. What if we use the permutations array to
      store the original element that was replaced? Answer no.
    
    Correct response:
      We are going to swap the elements and mark the previosly
      permutated element in perm. We will follow the cycle 
      until we reach a previously permutated element,
      That will mean that we completed a mini-cycle 
      and all elements in that mini-cycle are placed correctly
      where they should.  p.57

    Performance: O(n)
    Space: O(1)
'''


def apply_permutation(perm, A):
    '''
    Solution with new array
    result = [0] * len(A)
    for p, a in zip(perm, A):
        result[p] = a

    return result
    '''
    # In place
    for i in range(len(A)):
        _next = i
        while perm[_next] >= 0:
            A[i], A[perm[_next]] = A[perm[_next]], A[i]
            #_next = perm[_next]
            temp = perm[_next]
            perm[_next] -= len(perm)
            _next = temp
            
    perm[:] = [a + len(perm) for a in perm]
    return A
    

   


def apply_permutation_wrapper(perm, A):
    r = apply_permutation(perm, A)
    return r


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
