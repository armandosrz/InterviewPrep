from test_framework import generic_test
from list_node import ListNode

'''
Remember to create iterators that will help
you go and modify lists. 

Make sure they both have a reference to the 
same initial node
'''


def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    
    if L1:
        tail.next = L1
    if L2:
        tail.next = L2

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
