
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root is not None:
        print(root.data, end="-")
        preorder(root.left)
        preorder(root.right)




def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end="-")
        inorder(root.right)



def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="-")



root = Node("M")
root.left = Node("I")
root.right = Node("K")
root.left.left = Node("E")



print("DFS Methods in Tree")

print("\nPreorder Traversal:")
preorder(root)

print("\n\nInorder Traversal:")
inorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print()
