import sys
import heapq

N = int(sys.stdin.readline().strip())

max_h = [-1 * int(sys.stdin.readline().strip())]
print(-1*max_h[0])
min_h = []

max_len = 0
min_len = 0

for _ in range(N-1):
    x = int(sys.stdin.readline().strip())
    if max_h[0] >= x :
        heapq.heappush(max_h, -x)
        max_len += 1
    if max_h[0] < x:
        heapq.heappush(min_h, x)
        min_len += 1
        
    if max_len == min_len +2:
        heapq.heappush(min_h, -1 * heapq.heappop(max_h))
        min_len, max_len = min_len+1, max_len-1
        print(-1 * max_h[0])
        continue
    if max_len+1 == min_len:
        heapq.heappush(max_h, -1*heapq.heappop(min_h))
        min_len, max_len = min_len-1, max_len+1
        print(-1 * max_h[0])
    
    