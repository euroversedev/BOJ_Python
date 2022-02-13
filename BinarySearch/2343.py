import sys

N, M = map(int, input().split())
array = list(map(int, sys.stdin.readline().split()))

def check(volume):
    cnt = 1
    length = 0
    for num in array:
        if length + num > volume:
            cnt += 1
            length = num
        else:
            length += num
    if cnt > M:
        return False
    return True

ans = 0
def binary_search(start, end):
    global ans
    if start > end:
        return ans
    
    mid = (start+end) // 2
    
    if check(mid):
        ans = mid
        return binary_search(start, mid-1)
    else:
        return binary_search(mid+1, end)
    
result = binary_search(1, sum(array))
print(max(ans, max(array)))

