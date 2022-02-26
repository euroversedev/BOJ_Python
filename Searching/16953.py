from collections import deque


A, B = map(int, input().split())

def bfs():
    q = deque([(A, 1)])
    
    while q:
        num, cnt = q.popleft()
        if num == B:
            return cnt
        
        if num*2 <= B:
            q.append((num*2, cnt+1))
        if num*10 +1 <= B:
            q.append((num*10+1, cnt+1))
        
    return -1

print(bfs())

''' [review]
BFS를 써야하는 근거
필요한 연산의 최솟값 == 최단 거리 문제
'''