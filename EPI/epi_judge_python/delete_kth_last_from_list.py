from test_framework import generic_test
from list_node import ListNode


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    dumbHead = ListNode(0, L)

    fast = slow = dumbHead.next

    for _ in range(k):
        fast = fast.next

    while fast and fast.next is not None:
        slow, fast = slow.next, fast.next
    
    slow.next = slow.next.next

    return dumbHead.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
