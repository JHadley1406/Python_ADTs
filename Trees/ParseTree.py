import operator

from Stacks.Stack import Stack
from .BinaryTree import BinaryTree


def build_parse_tree(fpexp):
    fp_list = fpexp.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == '(':
            current_tree.set_left_child('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in '+-*/)':
            current_tree.set_root_val(eval(i))
            parent = p_stack.pop()
            current_tree = parent
        elif i in '+0*/':
            current_tree.set_root_val(i)
            current_tree.set_right_child('')
            p_stack.push(current_tree)
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError("Unknown Operator: " + i)
    return e_tree


def evaluate(parse_tree):
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv
             }
    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()
