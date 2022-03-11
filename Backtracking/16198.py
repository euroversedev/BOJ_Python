import sys

N = int(input())
energy = list(map(int, sys.stdin.readline().strip().split()))

def dfs(array):
    max_ = 0
    
    for i in range(1, len(array)-1):
        ret = dfs(array[:i]+array[i+1:]) + array[i-1]*array[i+1]
        if ret > max_:
            max_ = ret
    
    return max_
    
print(dfs(energy))