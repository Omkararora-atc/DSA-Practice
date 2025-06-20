### Find the nth node from the end of a linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def find(self,head,n):
        first=head
        second=head
        for i in range(n):
            if first is None:
                return None
            first = first.next
        while first:
            first = first.next
            second = second.next
        return second.data
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

    n = 2
    result = llist.find(llist.head, n)
    if result:
        print(f"The {n}th node from the end is: {result}")
    else:
        print("The linked list is shorter than n.")