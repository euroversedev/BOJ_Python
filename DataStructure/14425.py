import sys

N, M = map(int, sys.stdin.readline().strip().split())
S = set([sys.stdin.readline().strip() for _ in range(N)])

cnt = 0
for _ in range(M):
    if sys.stdin.readline().strip() in S: cnt+=1
        
print(cnt)
