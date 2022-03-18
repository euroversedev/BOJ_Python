import sys

N, M = map(int, sys.stdin.readline().strip().split())
array = [int(sys.stdin.readline().strip()) for _ in range(N)]

start, end = 1, 10**18
answer = 0
while start<= end:
    mid = (start+end) // 2
    
    sum_done = 0
    for num in array:
        sum_done += mid // num
    
    # print(mid, sum_done)
    if sum_done >= M:
        answer = mid
        end = mid -1
        
    else:
        start = mid + 1
        
print(answer)