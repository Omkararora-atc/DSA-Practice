### Find the middle of the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def count_ele(self,head):
        count=0
        curr=head
        while curr is not None:
            count += 1
            curr = curr.next
        curr=head
        for i in range(count//2):
            curr = curr.next
        return curr.data if curr else None
### Driver Code
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

    middle_value = ll.count_ele(ll.head)
    print(f"The middle element of the linked list is: {middle_value}")