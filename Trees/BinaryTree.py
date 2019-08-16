class BinaryTree:
    def __init__(self, root_obj):
        self._key = root_obj
        self._left_child = None
        self._right_child = None

    def set_left_child(self, new_node):
        if self._left_child is None:
            self._left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t._left_child = self._left_child
            self._left_child = t

    def set_right_child(self, new_node):
        if self._right_child is None:
            self._right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t._right_child = self._right_child
            self._right_child = t

    def get_right_child(self):
        return self._right_child

    def get_left_child(self):
        return self._left_child

    def set_root_val(self, obj):
        self._key = obj

    def get_root_val(self):
        return self._key

    def preorder(self, func=None):
        if func is None:
            print(self._key)
        else:
            func(self._key)
        if self._left_child:
            self.get_left_child().preorder()
        if self._right_child:
            self.get_right_child().preorder()
