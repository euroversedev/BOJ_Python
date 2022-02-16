class Node:
    def __init__(self, data):
        self.data = data
        
        
tree = dict()

tree['a'] = Node(1)
print(tree['a'].data)