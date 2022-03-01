import sys
from collections import deque

N = int(input())
array = []
for _ in range(N):
    c, r = map(int, sys.stdin.readline().strip().split())
    array.append((c-r, c+r))

array.sort()

tmp = []
for idx, (i, j) in enumerate(array):
    tmp.append((idx, i))
    tmp.append((idx, j))

tmp = deque(sorted(tmp, key = lambda x:x[1]))
stack = []
while tmp:
    idx, n = tmp.popleft()
    
    if stack and stack[-1] == idx:
        stack.pop()
    
    else:
        stack.append(idx)


if stack:
    print("NO")
else:
    print("YES")
