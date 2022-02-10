import sys
sys.setrecursionlimit(10**9)

N = int(input())
M = int(input())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

for i in range(N):
    for j in range(i+1, N):
        if board[i][j] == 1:
            a = find_parent(i+1)
            b = find_parent(j+1)
            if a < b: parent[b] = a
            else: parent[a] = b

flag = True
array = list(map(int, sys.stdin.readline().strip().split()))
for i in range(1, M):
    if find_parent(array[i-1]) == find_parent(array[i]):
        continue
    else:
        flag = False

if flag: print("YES")
else: print("NO")