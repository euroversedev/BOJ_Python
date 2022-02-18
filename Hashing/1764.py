import sys

N, M = map(int, input().split())
a = dict()
for _ in range(N):
    a[sys.stdin.readline().strip()] = False

for _ in range(M):
    b = sys.stdin.readline().strip()
    if b in a.keys():
        a[b] = True

result = [i for i in a.keys() if a[i]==True]
result.sort()
print(len(result))
print(*result, sep='\n')

