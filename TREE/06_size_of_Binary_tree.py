### find the size of binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def size(self, root):
        if root is None:
            return 0
        else:
            left_size = self.size(root.left)
            right_size = self.size(root.right)
            return left_size + right_size + 1
# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Size of binary tree is", root.size(root))  # Output: 5