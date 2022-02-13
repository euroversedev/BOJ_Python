import sys

N, M = map(int, input().split())
array = list(map(int, sys.stdin.readline().split()))

ans = 0
def binary_search(start, end):
    global ans
    if start > end:
        return ans
    
    mid = (start+end) // 2
    
    stack = array[:]
    cnt = 1
    sum_ = 0
    while stack:
        n = stack.pop()
        if sum_ + n <= mid:
            sum_ += n 
            continue
        else:    # 초과하는 경우
            cnt += 1
            sum_ = n
            

    if cnt <= M:
        ans = mid
        return binary_search(start, mid-1)
    else:
        return binary_search(mid+1, end)
    
    
result = binary_search(1, sum(array))
print(max(ans, max(array)))

