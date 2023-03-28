from typing import Union

Node = object
root = object


def find(root: Union[Node, None], key) -> bool:
    if root is None:
        return False

    if root.key == key:
        return True

    if key < root.key:
        return find(root.left, key)
    else:
        return find(root.right, key)


def insert(root: Union[Node, None], newnode: Node) -> Node:
    if root is None:
        return newnode

    if newnode.key < root.key:
        root.left = insert(root.left, newnode)
    else:
        root.right = insert(root.right, newnode)
    return root

# tree = insert(tree, Node(x, ))
