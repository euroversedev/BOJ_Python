import sys

dic = {}
N, M = map(int, input().split())
for _ in range(N):
    web, pw = sys.stdin.readline().strip().split()
    dic[web] = pw
    
for _ in range(M):
    print(dic[sys.stdin.readline().strip()])