import sys
import heapq

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    array = list(map(int, sys.stdin.readline().strip().split()))
    heapq.heapify(array)
    
    sum_ = 0
    for _ in range(N-1):
        a = heapq.heappop(array)
        b = heapq.heappop(array)
        heapq.heappush(array, a+b)
        sum_ += a + b
    print(sum_)
    