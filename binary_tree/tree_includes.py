class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_in_tree(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    return find_in_tree(root.left, value) or find_in_tree(root.right, value)

def find_in_tree_iterative(root, value):
    if root is None:
        return False
    stack = [root]
    while stack:
        node = stack.pop()
        if node.value == value:
            return True
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return False

if __name__ == "__main__":
    # Example usage
    a  = Tree('A')
    b  = Tree('B')
    c  = Tree('C')
    d  = Tree('D')
    e  = Tree('E')
    f  = Tree('F')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(find_in_tree(a, 'E'))  # True
    print(find_in_tree(a, 'Z'))  # False