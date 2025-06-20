### Remove Duplicates from a Sorted Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head= None
    def remove_duplicates(self,head):
        if head is None:
            return None
        curr = head
        while curr.next:
            if curr.data ==curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
### Driver code
if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(1)
    third = Node(2)
    fourth = Node(3)
    fifth = Node(3)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    print("Original Linked List:")
    llist.print_list()

    llist.remove_duplicates(llist.head)

    print("Linked List after removing duplicates:")
    llist.print_list()