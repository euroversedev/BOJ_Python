import sys
from collections import deque

N = int(input())
visited = [False] * (N+1)

# bfs
q = deque([(N, [N])])

while q:
    num, array = q.popleft()
    
    if num == 1:
        print(len(array)-1)
        print(*array)
        exit()
    
    if num % 3 == 0 and visited[num//3] == False:
        visited[num//3] = True
        q.append((num//3, array+[num//3]))
        
    if num % 2 == 0 and visited[num//2] == False:
        visited[num//2] = True
        q.append((num//2, array+[num//2]))
        
    if num - 1 > 0 and visited[num-1] == False:
        visited[num-1] = True
        q.append((num-1, array+[num-1]))
    