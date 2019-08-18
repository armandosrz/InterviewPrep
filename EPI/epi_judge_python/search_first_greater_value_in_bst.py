from test_framework import generic_test


def find_first_greater_than_k(tree, k):
    node, current = tree, None

    while node:
        if node.data > k:
            current, node = node, node.left
        else:
            node = node.right
    
    return current

    '''
    # in order o(n) solution
    def inOrder(node):
        if node is None:
            return None
        l = inOrder(node.left)
        if l:
            return l
        if node.data > k:
            return node
        r = inOrder(node.right)
        return r
    
    return inOrder(tree)
    '''


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
