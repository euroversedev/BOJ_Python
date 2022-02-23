import sys
import heapq

N = int(input())
dic = dict()
for _ in range(N):
    s, e = map(int, sys.stdin.readline().strip().split())
    if dic.get(e, -1) == -1:
        dic[e] = []
    dic[e].append(s)

cnt = 0
time = 0
for end, starts in sorted(dic.items()):

    for start in sorted(starts):
        if time <= start:
            time = end
            cnt += 1

print(cnt)