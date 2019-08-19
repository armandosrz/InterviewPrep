import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    def get_optimun(k, available):
        if k < 0:
            return 0
        
        if V[k][available] == -1:
            without = get_optimun(k-1, available)
            with_current = (0 if available < items[k].weight else (
                items[k].value + get_optimun(k-1, available - items[k].weight)
            ))
            V[k][available] = max(without, with_current)
        return V[k][available]

    V = [[-1] * (capacity + 1) for _ in items]
    return get_optimun(len(items)-1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
