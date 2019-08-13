from test_framework import generic_test


def is_balanced_binary_tree(tree):

    def check_balance(node, level):
        if not node:
            return (True, level - 1)

        balanced, left_level = check_balance(node.left, level+1)
        if not balanced:
            return (False, level)
        
        balanced, right_level = check_balance(node.right, level+1)
        if not balanced:
            return (False, level)

        balanced =  (abs(left_level - right_level)) <= 1

        return (balanced, max(left_level, right_level))

    
    return check_balance(tree, 0)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
