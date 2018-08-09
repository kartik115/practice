class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)

    def preorder(self, node):
        if node is None:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def levelorder(self):
        queue = list()
        queue.append(self.root)
        while len(queue) != 0:
            node = queue.pop(0)
            print(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)



t = BinaryTree()
t.root = Node(10)
t.root.left = Node(20)
t.root.left.left = Node(5)
t.root.left.right = Node(6)
t.root.right = Node(30)
t.root.right.left = Node(12)
t.root.right.right = Node(15)
t.root.right.left.right = Node(18)
print("in order")
t.inorder(t.root)
print("post order")
t.postorder(t.root)
print("pre order")
t.preorder(t.root)
print("level order")
t.levelorder()