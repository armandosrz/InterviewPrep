from test_framework import generic_test
from binary_tree_node import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder):
    inorder_dict = {val: index for index, val in enumerate(inorder)}
    
    def helper(i_start, i_finish, p_start, p_finish):
        if p_start >= p_finish or i_start >= i_finish:
            return None
        
        inorder_root_index = inorder_dict[preorder[p_start]]
        left_tree_size = inorder_root_index - i_start
        return BinaryTreeNode(
            preorder[p_start],
            helper(i_start, inorder_root_index, p_start+1, p_start + 1 + left_tree_size),
            helper(inorder_root_index + 1, i_finish, p_start + 1 + left_tree_size, p_finish) 
        )       


    return helper(0, len(inorder), 0, len(preorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
