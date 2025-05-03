class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sum_tree(root):
    if root is None:
        return 0
    return root.value + sum_tree(root.left) + sum_tree(root.right)

if __name__ == "__main__":
    # Example usage
    a  = Tree(3)
    b  = Tree(11)
    c  = Tree(4)
    d  = Tree(4)
    e  = Tree(2)
    f  = Tree(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print(sum_tree(a))  # Output: 25