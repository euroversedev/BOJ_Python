import sys
N, M = map(int, sys.stdin.readline().strip().split())
costs = [int(sys.stdin.readline().strip()) for _ in range(N)]


def binary_search(start, end):

    if start >= end:
        return start
    
    # 비용 mid
    mid = (start+end) // 2
    
    cnt = 1
    sum_ = costs[0]
    for cost in costs[1:]:
        if sum_ + cost > mid:
            cnt += 1
            sum_ = cost
            continue
        
        if sum_ + cost <= mid:
            sum_ += cost
    

    # 계획 M보다 적게 돈을 인출한 경우 => 더 낮은 최소비용
    if cnt <= M and mid >= max(costs):
        return binary_search(start, mid)
    
    else:
        return binary_search(mid+1, end)
        
print(binary_search(1, 10**9))