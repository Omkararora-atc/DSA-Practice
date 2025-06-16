### Insert at the given position in a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,):
        self.head = None
    def insert_at_position(self, head, key, position):
        new=Node(key)
        if position == 1:
            new.next = head
            return new
        current = head
        count = 1
        while current.next and count<position-1:
            current = current.next
            count += 1
        new.next = current.next
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
    position = 2
    ll.head = ll.insert_at_position(ll.head, key, position)

    # Print the linked list
    ll.print_list()  # Output: 1 -> 4 -> 2 -> 3 -> None
