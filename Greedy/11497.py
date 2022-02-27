import sys
from collections import deque

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    array = deque(sorted(list(map(int, sys.stdin.readline().strip().split()))))
    result = [0] * N
    for i in range((N+1)//2):
        result[i] = array.popleft()
        try:
            result[-(i+1)] = array.popleft()
        except:
            break
    
    max_ = 0
    for i in range(N):
        if max_ < abs(result[i]-result[i-1]):
            max_ = abs(result[i]-result[i-1])
            
    print(max_)
    
    