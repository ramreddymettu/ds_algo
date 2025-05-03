class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_min(root):
    if root is None:
        return float('inf')  # Return a large value for comparison
    return min(root.value, tree_min(root.left), tree_min(root.right))

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

    print(tree_min(a))  # Output: 25