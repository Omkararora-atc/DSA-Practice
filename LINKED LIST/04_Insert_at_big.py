### Insert at the beginning of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_big(self,head,key):
        new=Node(key)
        if head is None:
            return new
        new.next = head
        return new
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
### Driver code
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(2)
    second = Node(3)
    third = Node(4)

    ll.head.next = second
    second.next = third
    key = 1
    ll.head = ll.insert_big(ll.head, key)

    # Print the linked list
    ll.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> None