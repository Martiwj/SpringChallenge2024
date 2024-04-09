class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(tree_list):

    """
    This method converts a list representation of a binary tree into an actual binary tree structure.
    
    Args:
        tree_list (list): A list representation of a binary tree where each element corresponds to
                         a node's value. The list follows the level-order traversal of the binary tree,
                         with 'None' indicating absence of a node at that position.

    Returns:
        TreeNode: The root node of the constructed binary tree.

    Example:
        tree_list = [1, 2, 3, None, 4, 5, 6]
        construct_tree(tree_list) would return the root node of the binary tree:
               1
             /   \
            2     3
             \   / \
              4 5   6     
    """
    
    if not tree_list:
        return None

    root = TreeNode(tree_list[0])
    i = 1
    queue = [root]

    while i < len(tree_list):
        current_node = queue.pop(0)

        if i < len(tree_list) and tree_list[i] is not None:
            left_child = TreeNode(tree_list[i])
            current_node.left = left_child
            queue.append(left_child)

        i += 1

        if i < len(tree_list) and tree_list[i] is not None:
            right_child = TreeNode(tree_list[i])
            current_node.right = right_child
            queue.append(right_child)

        i += 1

    return root

def print_tree_array(root):

    """
    This method converts a binary tree back to a list representation.
    """
    
    output = []
    if not root:
        return

    level = [root]
    result = []

    while level:
        current_level = []
        for node in level:
            if node:
                current_level.append(node.val)
            else:
                current_level.append(None)  

        result.append(current_level)
        level = [child for node in level for child in (node.left, node.right) if child]

    for level in result:
        for l in level:
            output.append(l)
            
    print(output)
    
