import sys
import heapq

N = int(input())

result = 0
h = []
for i in range(N):
    d, w = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(h, (-w, d))

visit = [False] * (1001)
while h:
    w, d = heapq.heappop(h)
    
    for i in range(d, 0, -1):
        if visit[i] == False:
            visit[i] = True
            result += -w
            break
    
print(result)