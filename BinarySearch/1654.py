import sys

N, K = map(int, input().split())
length = [int(sys.stdin.readline().strip()) for _ in range(N)]

def binary_search(start, end):
    mid = (start+end) // 2
    if start > end:
        return mid
    
    if mid != 0:
        cnt = sum([leng//mid for leng in length])
    
    if cnt >= K:    # K개보다 많이 만든 경우
        return binary_search(mid+1, end)
    else:
        return binary_search(start, mid-1)

print(binary_search(1, max(length)))