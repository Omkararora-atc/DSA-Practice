### Find the maximum height of a binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def height(self, root):
        if root is None:
            return 0
        else:
            left_height=self.height(root.left)
            right_height=self.height(root.right)
            return max(left_height, right_height) + 1
# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Height of binary tree is", root.height(root))  # Output: 3
