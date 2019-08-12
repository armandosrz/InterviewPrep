from test_framework import generic_test

'''
The task is basically a bfs in which we return an 
array which all the elements in order, in which they
all return in the level they correspond.
'''

def binary_tree_depth_order(tree):
    if not tree:
        return []

    result = []

    queue = [(tree, 0)]

    while queue:
        current, depth = queue.pop(0)
        
        if depth > len(result)-1:
            result.append([current.data])
        else:
            result[depth].append(current.data)
        
        if current.left:
            queue.append((current.left, depth + 1))
        if current.right:
            queue.append((current.right, depth + 1))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
