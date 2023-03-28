def do_need_rotation():
    pass


root = object


def height(v):
    if v is None:
        return 0
    return v.height


def avl_insert(root, newnode):
    if root is None:
        return newnode

    if newnode.key < root.key:
        root.left = avl_insert(root.left, newnode)
        root.height = 1 + max(height(root.left), height(root.right))

        if height(root.left) == height(root.right) + 2:
            root = do_need_rotation(root)

        else:
            # аналогично вставке в левое поддерево
            pass

        return root
