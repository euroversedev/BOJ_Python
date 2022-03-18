import sys

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
len_word = [False] * 501
N, M = map(int, sys.stdin.readline().strip().split())
for _ in range(N):
    word = sys.stdin.readline().strip()
    trie.insert(word)
    len_word[len(word)] = True

cnt = 0
for _ in range(M):
    word = sys.stdin.readline().strip()
    if len_word[len(word)] == False:
        continue
    if trie.search(word):
        cnt += 1

print(cnt)