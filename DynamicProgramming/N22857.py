import sys

N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))
list_ = [1 if array[i]%2==1 else 0 for i in range(N)]

max_ = 0
for i in range(N):
    cnt_1 = 0
    cnt_0 = 0
    for j in range(i, -1, -1):
        if list_[j] == 1:
            cnt_1 += 1
        
        if cnt_1 == K + 1:
            if cnt_0 > max_: max_ = cnt_0
            break
            
        if list_[j] == 0:
            cnt_0 += 1
            
print(max_)