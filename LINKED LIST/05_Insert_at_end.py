### Insert the key at the end of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,head,key):
        new=Node(key)
        if head is None:
            return new
        current = head
        while current.next is not None:
            current = current.next
        current.next = new
        return head
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
### Driver code
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third
    key = 4
    ll.head = ll.insert(ll.head, key)

    # Print the linked list
    ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> None
