class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
class BST:
    def insert(self,root,key):
        if root is None:
            return Node(key)
        if root.val>key:
            root.left = self.insert(root.left, key)
        elif root.val<key:
            root.right = self.insert(root.right, key)
        return root
    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=' ')
            self.inorder_traversal(root.right)
# Example usage:
if __name__ == "__main__":
    bst = BST()
    root = None
    keys = [10, 5, 15, 3, 7, 20]

    for key in keys:
        root = bst.insert(root, key)
    print("Inorder traversal of the BST:")
    bst.inorder_traversal(root)
    print()


