import sys
N, M = map(int, sys.stdin.readline().strip().split())
costs = [int(sys.stdin.readline().strip()) for _ in range(N)]

def binary_search(start, end):
    if start >= end:
        return start
    
    # 비용 mid
    mid = (start+end) // 2
    
    cnt = 0
    sum_ = 0
    for cost in costs:
        if sum_ + cost > mid:
            cnt += 1
            sum_ = cost
        
        if sum_ + cost <= mid:
            sum_ += cost
        
    if sum_ > 0:
        cnt += 1
    
    # 계획 M보다 적게 돈을 인출한 경우 => 더 낮은 최소비용
    if cnt < M:
        return binary_search(start, mid-1)
    
    else:
        return binary_search(mid, end)
        

print(binary_search(1, 10**9))