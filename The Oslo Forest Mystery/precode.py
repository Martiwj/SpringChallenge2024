class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_tree(tree_list):
    if not tree_list:
        return None

    root = TreeNode(tree_list[0])
    i = 1
    queue = [root]

    while i < len(tree_list):
        current_node = queue.pop(0)

        # Handle left child
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
    