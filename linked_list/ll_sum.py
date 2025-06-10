class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def getLLValues(head):
    values = 0
    current = head
    while current is not None:
        values += current.data
        current = current.next
    return values

def getLLValuesRecursive(node):
    if node is None:
        return 0
    return node.data + getLLValuesRecursive(node.next)

if __name__ == "__main__":
    # Create a linked list
    head = Node(5)
    second = Node(3)
    third = Node(1)
    fourth = Node(4)
    fifth = Node(9)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = None

    print(getLLValues(head))
    print(getLLValuesRecursive(head))