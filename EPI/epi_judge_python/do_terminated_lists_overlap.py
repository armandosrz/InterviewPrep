import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook



def overlapping_no_cycle_lists(l0, l1):
    '''
    visited = set()
    while l0 and l0.next is not None:
        visited.add(id(l0))
        l0 = l0.next
    
    while l1 and  l1.next is not None:
        if id(l1) in visited:
            return l1
        l1 = l1.next
    '''
    def get_len(node):
        curr = node
        size = 0
        while curr:
            curr = curr.next
            size += 1
        return size
    
    l0_len, l1_len = get_len(l0), get_len(l1)

    if l0_len > l1_len:
        l0, l1 = l1, l0 # we treat l1 as the long
    
    for _ in range(abs(l0_len - l1_len)):
        l1 = l1.next
    
    while l0 and l1:
        if l1 is l0:
            return l0
        
        l0, l1 = l0.next, l1.next
    
    return None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(
        functools.partial(overlapping_no_cycle_lists, l0, l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_terminated_lists_overlap.py",
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
