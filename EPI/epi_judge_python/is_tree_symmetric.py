from test_framework import generic_test

'''
In this case we need to compute the 
mirror of the left side.
'''
def is_symmetric(tree):
    if not tree:
        return True
    def is_mirror(l, r):
        if not l and not r:
            return True
        if l and not r or r and not l:
            return False
        
        return is_mirror(l.left, r.right) and is_mirror(l.right, r.left) and l.data == r.data

    return is_mirror(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
