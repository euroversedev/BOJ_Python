import sys

N, K = map(int, sys.stdin.readline().strip().split())

# a n t i c 제거
words = [set(sys.stdin.readline().strip()[4:-4]) for _ in range(N)]


tmp = []
for i in range(N):
    for ch in ['a', 'n', 't', 'i', 'c']:
        try:
            words[i].remove(ch)
        except:
            continue
            
        
print(words)
