import sys

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

tree = dict()

N = int(sys.stdin.readline().strip())
for _ in range(N):
    pa, lc, rc = sys.stdin.readline().strip().split()
    
    tree[pa] = ['a', 'a']
    if lc != '.': tree[pa][0] = lc
    if rc != '.': tree[pa][1] = rc

        
def preorder(pa):
    if pa not in tree.keys():
        return
    
    print(pa, end='')
    if tree[pa][0] != 'a': preorder(tree[pa][0])
    if tree[pa][1] != 'a': preorder(tree[pa][1])
            
def inorder(pa):
    if pa not in tree.keys():
        return
    
    if tree[pa][0] != 'a': inorder(tree[pa][0])
    print(pa, end='')
    if tree[pa][1] != 'a': inorder(tree[pa][1])
            
def postorder(pa):
    if pa not in tree.keys():
        return

    if tree[pa][0] != 'a': postorder(tree[pa][0])
    if tree[pa][1] != 'a': postorder(tree[pa][1])
    print(pa, end='')       
    
            
            
preorder('A')
print()
inorder('A')
print()
postorder('A')

    