from collections import deque

q = deque([1])
a = q.popleft()
b = q.popleft()
print(a, b)