from test_framework import generic_test
import heapq

def online_median(sequence):
   
    high = []
    low = []

    result = []

    for x in sequence:
        heapq.heappush(low, -heapq.heappushpop(high, x))

        if len(low) > len(high):
            heapq.heappush(high, heapq.heappop(low) * -1)
        
        result.append(0.5 * (high[0] + (-low[0]))
                      if len(low) == len(high) else high[0])
    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
