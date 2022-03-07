import sys
N, M = map(int, input().split())
array = [int(sys.stdin.readline().strip()) for _ in range(M)]

def binary_search(start, end):
    # mid가 최소 질투심일때 성립하는지 체크
    if start >= end:
        return start
    
    mid = (start + end) // 2
    
    cnt = 0
    for num in array:
        cnt += (num+(mid-1)) // mid
    
    # 성립하는 경우
    if cnt <= N:
        return binary_search(start, mid)
        
    else:
        return binary_search(mid+1, end)
    
print(binary_search(1, max(array)))
