### write a code to show the preorder traversal of a binary tree
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def preorder(self, root):
        if root:
            print(root.value, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Preorder traversal of binary tree is")
    root.preorder(root)  # Output: 1 2 4 5 3
    