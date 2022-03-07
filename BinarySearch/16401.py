import sys
from bisect import bisect_left
sys.setrecursionlimit(10**9)

M, N = map(int, input().split())
snack = list(map(int, sys.stdin.readline().strip().split()))
snack.sort()

def binary_search(start, end):
    mid = (start+end)//2
    
    if end < start:    
        return mid

    cnt = 0
    for length in snack:
        cnt += length // mid
    
    # mid로 과자를 나눠줄 수 있는 경우 => 더 큰거 찾기
    if cnt >= M:
        return binary_search(mid+1, end)
    
    # mid로 과자를 나눠줄 수 없는 경우 => 더 작은 과자 찾기
    else:
        return binary_search(start, mid-1)
        

print(binary_search(1, max(snack)))


'''
첫번쨰 제출 풀이
def binary_search(start, end):
    if start >= end:
        return start

    mid = (start+end+1)//2
    
    cnt = 0
    for length in snack:
        cnt += length // mid
    
    # mid로 과자를 나눠줄 수 있는 경우 => 더 작은거
    if cnt >= M:
        return binary_search(mid, end)
    
    # mid로 과자를 나눠줄 수 없는 경우 => 더 작은 과자 찾아야함
    else:
        return binary_search(start, mid-1)
'''