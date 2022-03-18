import sys
from collections import deque

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.links = {}
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.links:
                node.links[ch] = TrieNode()
            
            node = node.links[ch]
        node.isEnd = True
    
    # bfs말고 dfs로 했어야 했네...
    '''
    def traverse(self):
        node = self.root
        q = deque([(node.links[key], key, 0) for key in sorted(node.links.keys())])
        
        while q:
            node, data, depth = q.popleft()
            print(data + "--"*depth)
            
            for nextKey in sorted(node.links.keys()):
                q.append((node.links[nextKey], nextKey, depth+1))
    '''
    def recurTraverse(self, node, data, depth):
        print("--"*depth+data, sep='')
        
        for key in sorted(node.links.keys()):
            self.recurTraverse(node.links[key], key, depth+1)
            
    def traverse(self):
        node = self.root
        for key in sorted(node.links.keys()):
            self.recurTraverse(node.links[key], key, 0)
    

            
    def search(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.links:
                return False
            node = node.links[ch]
        
        if node.isEnd:
            return True
        else:
            return False
            

trie = Trie()
N = int(input())
for _ in range(N):
    K, *words = sys.stdin.readline().strip().split()
    trie.insert(words)
    
trie.traverse()
    