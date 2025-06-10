class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def getLLValues(head):
    values = []
    current = head
    while current is not None:
        values.append(current.data)
        current = current.next
    return values

def getLLValuesRecursive(node):
    if node is None:
        return []
    return [node.data] + getLLValuesRecursive(node.next)

if __name__ == "__main__":
    # Create a linked list
    head = Node('A')
    second = Node('B')
    third = Node('C')
    fourth = Node('D')
    fifth = Node('E')

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = None

    print(getLLValues(head))
    print(getLLValuesRecursive(head))