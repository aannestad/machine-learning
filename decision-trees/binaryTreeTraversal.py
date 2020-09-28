# Binary tree traversal

class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)   # initialize tree with a root

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("traversal_type " + str(traversal_type) + " is not supported")
            return False

    def preorder_print(self, currentNode, accPath):
        """Root -> Left -> Right"""
        if currentNode != None:
            accPath += (str(currentNode.value) + "-") # Add current node to accumulated path
            accPath = self.preorder_print(currentNode.left, accPath) # Left subtree recursion
            accPath = self.preorder_print(currentNode.right, accPath) # Right subtree recursion
        return accPath

    def inorder_print(self,currentNode,accPath):
        """Left -> Root -> Right"""
        if currentNode != None:
            accPath = self.inorder_print(currentNode.left, accPath)
            accPath += (str(currentNode.value) + "-")
            accPath = self.inorder_print(currentNode.right, accPath)
        return accPath

    def postorder_print(self,currentNode,accPath):
        """Left -> Right -> Root"""
        if currentNode != None:
            accPath = self.postorder_print(currentNode.left, accPath)
            accPath = self.postorder_print(currentNode.right, accPath)
            accPath += str(currentNode.value) + "-"
        return accPath

# Testing -----------------------------------------------------------
# Build the following tree:

#        1
#      /   \
#    2       3
#   /  \    /  \
#  4    5  6    7  

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("The value of right leaf node: " + str(tree.root.right.right.value))
print("Pre-oder traverse: " + tree.print_tree("preorder"))
print("In-order traverse: " + tree.print_tree("inorder"))
print("Post-order traverse: " + tree.print_tree("postorder"))