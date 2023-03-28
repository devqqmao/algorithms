import random


class Node:
    def __init__(self, value):
        self.key = value
        self.priority = random.randint(0, 2 ** 10)
        self.left = None
        self.right = None
        self.size = 1


def size(tree):
    return tree.size if tree is not None else 0


def update(tree):
    if tree is not None:
        tree.size = 1 + size(tree.l) + size(tree.r)


def find_kth_element(tree, k):
    if size(tree.left) == k:
        return tree.key
    elif size(tree.left) > k:
        return find_kth_element(tree.left, k)
    else:
        return find_kth_element(tree.right, k - size(tree.left) - 1)


def get_size(tree):
    return tree.size if tree is not None else 0


def update_size(tree):
    if tree is not None:
        tree.size = 1 + get_size(tree.left) + get_size(tree.right)


def split(tree, value):
    if tree is None:
        return (None, None)
    elif tree.key > value:
        left, tree.left = split(tree.left, value)
        right = tree
    else:
        tree.right, right = split(tree.right, value)
        left = tree
    update_size(tree)
    return (left, right)


def merge(left, right):
    if left is None or right is None:
        return right if right is not None else left
    elif left.priority > right.priority:
        left.right = merge(left.right, right)
        update_size(left)
        return left
    else:
        right.left = merge(left, right.left)
        update_size(right)
        return right


def insert(tree, node):
    if tree is None:
        return node
    elif tree.priority < node.priority:
        left, right = split(tree, node.key)
        node.left, node.right = left, right
        update_size(node)
        return node
    elif node.key < tree.key:
        tree.left = insert(tree.left, node)
    else:
        tree.right = insert(tree.right, node)
    update_size(tree)
    return tree


def remove(tree, value):
    if tree is None:
        return None
    elif tree.key == value:
        return merge(tree.left, tree.right)
    elif value < tree.key:
        tree.left = remove(tree.left, value)
    else:
        tree.right = remove(tree.right, value)
    update_size(tree)
    return tree


n = int(input())
tree = None
length = 0
for i in range(n):
    inputs = input().split()
    command = int(inputs[0])
    value = int(inputs[1])
    if command == 1:
        node = Node(value)
        tree = insert(tree, node)
        length += 1
    elif command == 0:
        print(find_kth_element(tree, length - value))
    elif command == -1:
        tree = remove(tree, value)
        length -= 1
