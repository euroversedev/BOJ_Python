import sys

N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

now = []
tmp = []
cnt = 0
for num in array:
    print(now, 99, tmp)
    if len(now) < N and num not in now:
        now.append(num)
        continue
    
    if len(now) == N:
        
        if num not in tmp:
            tmp.append(num)
        
        if len(tmp) > N:
            cnt += len(set(tmp)-set(now))
            now = tmp[-1*N:]
            tmp = []    
    

    # if len(now) < N and num not in now:
    #     now.append(num)
    #     continue
        
    # if len(now) == N and num not in now:
    #     if len(tmp) < N and num not in tmp:
    #         tmp.append(num)
        
    #     if len(tmp) == N:
    #         cnt += N
    #         now = tmp
    #         tmp = []
        
cnt += len(tmp)
print(cnt)