from test_framework import generic_test


def search_first_of_k(A, k):
    L, U = 0, len(A)-1
    index = -1
    while L <= U:
        mid = L + (U-L)//2
        if A[mid] < k:
            L = mid + 1
        elif A[mid] > k:
            U = mid -1
        else:
            index = mid
            U = mid - 1

    return index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
