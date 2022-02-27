import sys
import heapq

N, M = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
heapq.heapify(array)

for _ in range(M):
    a = heapq.heappop(array)
    b = heapq.heappop(array)
    heapq.heappush(array, a+b)
    heapq.heappush(array, a+b)
print(sum(array))
