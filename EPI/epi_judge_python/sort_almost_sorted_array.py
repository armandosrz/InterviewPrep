from test_framework import generic_test
import heapq

def sort_approximately_sorted_array(sequence, k):
    result = []
    sequence = list(sequence)
    for i in range(0, len(sequence), k):
        k_heap = sequence[i:i+k]
        heapq.heapify(k_heap)
        while k_heap:
            result.append(heapq.heappop(k_heap))

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
