from test_framework import generic_test
from list_node import ListNode

def reverse_sublist(L, start, finish):
    head = sublist_head = ListNode(0, L)

    for i in range(1, start):
        print (i, start)
        sublist_head = sublist_head.next

    curr = sublist_head.next
    for _ in range(finish - start):
        temp = curr.next
        curr.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
