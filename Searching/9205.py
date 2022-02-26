import sys
from collections import deque

def bfs(start, end, list_):
    visited = [False] * len(list_)
        
    q = deque([start])    
    while q:
        y, x = q.popleft()

        if (y, x) == end: return "happy"
        
        for idx, (storeY, storeX) in enumerate(list_):
            if visited[idx] == False:
                dis = abs(storeY-y) + abs(storeX-x)
                if dis <= 1000:
                    q.append(list_[idx])
                    visited[idx] = True
    return "sad"


T = int(input())
for _ in range(T):
    # 편의점의 수 n
    n = int(sys.stdin.readline().strip())
    
    # 상근 위치 start
    start = tuple(map(int, sys.stdin.readline().strip().split()))
    
    # 편의점 리스트 list_
    list_ = [tuple(map(int, sys.stdin.readline().strip().split()))
             for _ in range(n)]
    
    # 페스티벌 위치 end
    end = tuple(map(int, sys.stdin.readline().strip().split()))
    list_.append(end)
    print(bfs(start, end, list_))