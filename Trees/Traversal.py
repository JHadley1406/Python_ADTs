
def print_node(val):
    print(val)


def preorder(tree, func=print_node):
    if tree is not None:
        func(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree, func=print_node):
    if tree is not None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        func(tree.get_root_val)


def inorder(tree, func=print_node):
    if tree is not None:
        inorder(tree.get_left_child())
        func(tree.get_root_val)
        inorder(tree.get_right_child())
