### write a code to show the postorder traversal of a binary tree
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=' ')
# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Postorder traversal of binary tree is")
    root.postorder(root)  # Output: 4 5 2 3 1
    