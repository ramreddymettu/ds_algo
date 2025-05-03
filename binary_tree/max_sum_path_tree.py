class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_sum_path(root):
    if root is None:
        return -float('inf')
    if root.left is None and root.right is None:
        return root.value
    return root.value + max(max_sum_path(root.left), max_sum_path(root.right))

if __name__ == "__main__":
    # Example usage
    a  = Tree(5)
    b  = Tree(11)
    c  = Tree(3)
    d  = Tree(4)
    e  = Tree(2)
    f  = Tree(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(max_sum_path(a))