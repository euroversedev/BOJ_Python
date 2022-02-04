import sys
import heapq

N = int(input())
h = [int(sys.stdin.readline().strip()) for _ in range(N)]
heapq.heapify(h)

result = 0
while h:
    K = heapq.heappop(h)
    if len(h) > 0 :
        K += heapq.heappop(h)
    
    result += K
    
    if len(h) > 0:
        heapq.heappush(h, K)

print(result)
