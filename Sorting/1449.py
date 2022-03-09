import sys
N, L = map(int, input().split())
array = sorted(list(map(int, sys.stdin.readline().strip().split())))

start = array[0]
cnt = 0
for i in array[1:]:
    if i-start <= L-1:
        continue
    
    else: # i-start >= L-1:
        cnt += 1
        start = i
        
print(cnt+1)