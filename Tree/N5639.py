import sys
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(int(sys.stdin.readline().strip()))
def insert_(parent, key):
    if parent.data > key:
        if parent.left != None: insert_(parent.left, key)
        else: parent.left = Node(key)
    
    if parent.data < key:
        if parent.right != None: insert_(parent.right, key)
        else: parent.right = Node(key)
    
def postorder(parent):
    if parent == None: return
    postorder(parent.left)
    postorder(parent.right)
    print(parent.data)

while True:
    key = sys.stdin.readline().strip()
    if key == "": break
    insert_(root, int(key))

postorder(root)

    
        