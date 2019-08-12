from test_framework import generic_test


def reverse_sublist(L, start, finish):
    stack, count = [], 1
    head = iterator = L
    while L:
        if count >= start and count <= finish:
            stack.append(L.data)
        
        count +=1
        L = L.next
    
    count = 1
    while iterator:
        if count >= start and count <= finish:
            iterator.data = stack.pop()
        count +=1
        iterator = iterator.next

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
