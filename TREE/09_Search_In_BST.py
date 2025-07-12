class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def search_in_bst(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search_in_bst(root.left, key)
    return search_in_bst(root.right, key)
# Example usage:
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.right = Node(20)

    key_to_search = 7
    result = search_in_bst(root, key_to_search)
    if result:
        print(f"Node with key {key_to_search} found: {result.val}")
    else:
        print(f"Node with key {key_to_search} not found.")

