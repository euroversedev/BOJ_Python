import sys
sys.setrecursionlimit(10**6)

N = int(input())
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = int(sys.stdin.readline().strip())

def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
    
    
for i in range(1, N+1):
    find_parent(i)
    
def dfs(x):
    graph[x]
    
    
    
flag = [False] * (N+1)
for i in range(1, N+1):
    dfs(i)

print(flag.count(True))
for i in range(1, N+1):
    if flag[i] == True: print(i)

''' review
싸이클 문제 같은데.. 음..

'''