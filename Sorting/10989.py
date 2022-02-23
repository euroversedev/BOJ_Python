import sys
N = int(input())

cnt = [0]*10001

for _ in range(N):
    cnt[int(sys.stdin.readline().strip())] += 1

for i in range(10001):
    if cnt[i] > 0:
        for _ in range(cnt[i]):
            print(i)