### write the code to show the inorder traversal of a binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val,end=' ')
            self.inorder(root.right)
# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal of binary tree is")
    root.inorder(root)  # Output: 4 2 5 1 3
