class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def find_maximum(self, root):
        if root is None:
            return float('-inf')
        else:
            left_max = self.find_maximum(root.left)
            right_max = self.find_maximum(root.right)
            return max(root.data, left_max, right_max)
# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Maximum value in binary tree is", root.find_maximum(root))  # Output: 5