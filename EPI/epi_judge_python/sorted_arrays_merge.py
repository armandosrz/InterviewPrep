from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays):
    min_heap = []

    iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(iters):
        next_elem = next(it, None)
        if next_elem is not None:
            heapq.heappush(min_heap, (next_elem, i))

    result = []
    while min_heap:
        elem, index = heapq.heappop(min_heap)
        next_iter = iters[index]
        result.append(elem)
        next_elem = next(next_iter, None)
        if next_elem is not None:
            heapq.heappush(min_heap, (next_elem, index))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
