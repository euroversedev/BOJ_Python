import sys
import heapq

T = int(input())
for _ in range(T):
    K = int(sys.stdin.readline().strip())
    
    h = []
    for _ in range(K):
        cmd, n = sys.stdin.readline().strip().split()
        n = int(n)
        
        if cmd == "I":
            heapq.heappush(h, n)
        
        if cmd == "D" and h:
            if n > 0:    # 최댓값 삭제
                h = heapq.nlargest(len(h), h)[1:]
                heapq.heapify(h)
            if n < 0:    # 최솟값 삭제
                heapq.heappop(h)

    if h:
        print(max(h), min(h));
    else:
        print("EMPTY")