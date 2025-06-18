### Sorted Insert Linked List in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def ins_element(self,head,x):
        temp=Node(x)
        if head is None:
            return temp
        elif x< head.data:
            temp.next = head
            return temp
        else:
            curr=head
            while curr.next is not None and curr.next.data < x:
                curr = curr.next
            temp.next = curr.next
            curr.next = temp
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
    second = Node(3)
    third = Node(5)

    ll.head.next = second
    second.next = third

    print("Original Linked List:")
    ll.print_list()

    x = 2
    ll.head = ll.ins_element(ll.head, x)

    print(f"Linked List after inserting {x}:")
    ll.print_list()
    