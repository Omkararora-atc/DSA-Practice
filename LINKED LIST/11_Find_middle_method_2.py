#### Finding middle of a linked list using two pointers method
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def find(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data if slow else None
# ### Driver Code
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    ll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    print("Original Linked List:")
    curr = ll.head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

    middle_value = ll.find(ll.head)
    print(f"The middle element of the linked list is: {middle_value}")