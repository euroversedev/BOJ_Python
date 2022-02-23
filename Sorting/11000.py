import sys
import heapq

N = int(input())
h1 = [tuple(map(int, sys.stdin.readline().strip().split()))
     for _ in range(N)]

# 종료 시간이 들어갈 우선순위 큐(= 강의실 수)
h2 = [0]
heapq.heapify(h1)

max_ = 0
while h1:
    start, end = heapq.heappop(h1)
    
    if start >= h2[0]:
        heapq.heappop(h2)
        heapq.heappush(h2, end)
        continue
        
    else: 
        heapq.heappush(h2, end)
        max_ = max(max_, len(h2))
    
print(max_)

