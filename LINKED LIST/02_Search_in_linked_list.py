### You are given a singly linked list of n elements, and also an element x.
# You need to find if x is present in the linked list or not.
# Return true if x is present else returns false

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self,val=None):
        self.head=None
    def Search(self,head,x):
        if head is None:
            return False
        curr=head
        while curr:
            if curr.val==x:
                return True
            curr=curr.next
        return False
### Example usage, driver code is generated by the AI.
if __name__ == "__main__":
    # Create a linked list with 3 nodes
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    # Search for an element in the linked list
    x = 2
    if ll.Search(ll.head, x):
        print(f"Element {x} is present in the linked list.")
    else:
        print(f"Element {x} is not present in the linked list.")

