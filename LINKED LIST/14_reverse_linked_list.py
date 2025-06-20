class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
class LinkedList:
        def __init__(self):
            self.head = None
        def reverse(self,head):
            prev=None
            curr=head
            while curr:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev
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
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    print("Original Linked List:")
    llist.print_list()

    llist.head = llist.reverse(llist.head)

    print("Reversed Linked List:")
    llist.print_list()