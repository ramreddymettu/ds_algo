from collections import deque
class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
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

    bfs(a)