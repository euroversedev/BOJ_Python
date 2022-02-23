import sys
import heapq

h = []

N = int(input())
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    
    if n == 0:
        if h:
            x = []
            x.append(heapq.heappop(h))

            while h and x[0][0] == h[0][0]:
                x.append(heapq.heappop(h))
            x = sorted(x, key = lambda k: k[1])
            print(x[0][1])
            for i in range(1, len(x)):
                heapq.heappush(h, x[i])
                
        else: print(0)
    
    else:
        heapq.heappush(h, (abs(n), n))