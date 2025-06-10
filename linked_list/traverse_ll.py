class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_linked_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

def traverse_linked_list_recursive(node):
    if node is None:
        return
    print(node.data)
    traverse_linked_list_recursive(node.next)

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

    #traverse_linked_list(head)
    traverse_linked_list_recursive(head)