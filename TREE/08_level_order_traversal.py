### Level order traversal of a binary tree

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def level_order(self, root):
        if not root:
            return
        queue=deque()
        queue.append(root)

        while queue:
            current = queue.popleft()
            print(current.value, end=' ')

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(9)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level order traversal of binary tree is")
    root.level_order(root)