import sys

N = int(input())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

dic = dict()
for i in range(N):
    for j in range(i+1, N):
        k = array[i]+array[j]
        if not (array[0] <= k <= array[-1]):
            break
            
        if k not in dic.keys():
            dic[k] = [(i, j)]
        else:
            dic[k].append((i, j))

cnt = 0
for k in range(N):
    if array[k] in dic.keys():
        for i, j in dic[array[k]]:
            if k not in (i, j):
                cnt += 1
                break
print(cnt)