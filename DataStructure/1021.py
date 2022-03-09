import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
q = deque(range(1, N+1))

array = list(map(int, sys.stdin.readline().strip().split()))
result = 0
for num in array:
    # num은 현재 뽑아내야하는 수
    print(q)
    
    len_ = len(q)
    idx = q.index(num)
    
    if idx <= len_//2:
        q.rotate(-1* idx)
        result += idx
        
    else:
        q.rotate(len_-idx)
        result += len_-idx
    
    q.popleft()

print(result)
'''
1 [2] 3 4 [5] 6 7 8 [9] 10

3 4 [5] 6 7 8 [9] 10 1

[9] 10 1 3 4 [5] 6 7 8

'''
    