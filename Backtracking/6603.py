import sys

def dfs(array, idx, K, sequence):
    if len(sequence) == 6:
        print(*sequence)
    
    for i in range(idx, K):
        dfs(array, i+1, K, sequence+[array[i]])

while True:
    K, *S = map(int, sys.stdin.readline().strip().split())
    if K == 0: exit()
    
    dfs(S, 0, K, [])
    print()