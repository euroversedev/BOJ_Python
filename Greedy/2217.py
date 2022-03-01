import sys

N = int(input())

dic_ = dict()
for i in range(N):
    n = int(sys.stdin.readline().strip())
    if dic_.get(n, -1) == -1:
        dic_[n] = 0
    dic_[n] += 1

k = N
max_ = 0

for t, cnt in sorted(dic_.items()):
    if max_ < t*k:
        max_ = t*k
    k -= cnt
    
print(max_)
    
    
    