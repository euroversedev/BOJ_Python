import sys
from collections import deque

N = int(input())
q = deque(enumerate(map(int, sys.stdin.readline().strip().split())))

idx, stride = q.popleft()
result = [idx+1]
while q:
    # 번호가 양수
    if stride > 0:
        q.rotate(-stride)
        idx, stride = q.pop()
        result.append(idx+1)
        continue
        
    # 번호가 음수
    else:
        q.rotate(-stride)
        idx, stride = q.popleft()
        result.append(idx+1)
        continue
    

print(*result, sep=' ')

