from collections import deque

F, S, G, U, D = map(int, input().split())

visited = set([S])
q = deque([(S, 0)])

while q:
    now, depth = q.popleft()
    
    if now == G:
        print(depth)
        exit()
        
    if 1<=now+U<=F and now+U not in visited:
        visited.add(now+U)
        q.append((now+U, depth+1))
        
    if 1<=now-D<=F and now-D not in visited:
        visited.add(now-D)
        q.append((now-D, depth+1))
        
print("use the stairs")