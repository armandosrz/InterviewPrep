from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    result = []

    ''' 
    an inorder search of a bst returns all items 
    sorted.

    if we reverse and in order, we obtain the items
    sorted in descending order.
    '''
    def reverse_traverse(node):
        if not node:
            return
        reverse_traverse(node.right)
        if len(result) == k:
            return
        result.append(node.data)
        if len(result) == k:
            return
        reverse_traverse(node.left)
        return   
    
    reverse_traverse(tree)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
