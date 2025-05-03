class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
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

    dfs(a)