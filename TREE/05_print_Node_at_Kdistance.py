### Print nodes at k distance from root
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def print_k(self,root,k):
        if root is None:
            return
        if k==0:
            print(root.data,end=' ')
        else:
            self.print_k(root.left,k-1)
            self.print_k(root.right,k-1)
# Driver code
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    k = 2
    print(f"Nodes at distance {k} from root are:")
    root.print_k(root, k)  # Output: 4 5

