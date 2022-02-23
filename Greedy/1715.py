import sys
import heapq

N = int(input())
h = [int(sys.stdin.readline().strip()) for _ in range(N)]
heapq.heapify(h)

result = 0
for _ in range(N-1):
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    heapq.heappush(h, a+b)
    result += a + b

print(result)
