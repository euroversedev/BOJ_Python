import sys

K = int(input())
tree = [[] for _ in range(K)]
buildings = list(map(int, sys.stdin.readline().strip().split()))

def recursion(array, depth, start, end):
    mid = (start+end)//2
    tree[depth].append(array[mid])
    
    if depth < K-1:
        recursion(array, depth+1, start, mid-1)
        recursion(array, depth+1, mid+1, end)

recursion(buildings, 0, 0, 2**K-2)
for i in range(K):
    print(*tree[i])
    
    