import sys


class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        
# 전위 순회 결과를 토대로 트리 구성하기
root = Node(int(sys.stdin.readline().strip()))
now = root
while True:
    try:
        data = int(sys.stdin.readline().strip())
    except:
        break
        
    newnode = Node(data)
    if now.data > newnode.data:
        now.left = newnode
        newnode.parent = now
        now = now.left
        continue
    
    elif now.data < newnode.data and now.parent is not None and now.parent.data > newnode.data:
        now.right = newnode
        newnode.parent = now
        now = now.right
        continue
        
    elif now.parent is not None and now.parent.data < newnode.data:
        while now.parent is not None and now.parent.data < newnode.data:
            now = now.parent
        
        now.right = newnode
        newnode.parent = now
        now = now.right
        continue
        
    elif now.data < newnode.data:
        now.right = newnode
        newnode.parent = now
        now = now.right

def post_order(Node):
    if Node.left is not None:
        post_order(Node.left)
    if Node.right is not None:
        post_order(Node.right)
    print(Node.data)
    
post_order(root)
    



'''
pre/in/post
'''