### Delete the last node of a linked list in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def delete_node(self, head):
        if head is None:
            return None
        if head.next is None:
            return None
        curr=head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        return head
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# ### Driver Code
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    print("Original Linked List:")
    ll.print_list()

    ll.head = ll.delete_node(ll.head)

    print("Linked List after deleting the last node:")
    ll.print_list()

