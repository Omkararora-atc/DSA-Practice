### Given a linked list of size n, you have to delete the head of the linked list and return the new head.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def delete_head(self):
        if self.head is None:
            return None
        new_head = self.head.next
        self.head = new_head
        return new_head

# Driver code
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    # Delete the head of the linked list
    new_head = ll.delete_head()

    # Print the new head value
    if new_head:
        print(f"New head value after deletion: {new_head.val}")  # Output: 2
    else:
        print("The linked list is now empty.")
