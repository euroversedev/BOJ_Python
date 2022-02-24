import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

array = [[None] * (N+1) for _ in range(N+1)]
for _ in range(M):
    big, small = map(int, sys.stdin.readline().strip().split())
    array[big][small] = True
    array[small][big] = False
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if array[i][k] == None or array[k][j] == None:
                continue
            
            if array[i][k] == array[k][j]:
                array[i][j] = array[i][k]
                array[j][i] = not array[i][k]

for i in range(1, N+1):
    cnt_ = 0
    for j in range(1, N+1):
        if array[i][j] is None:
            cnt_ += 1
    print(cnt_-1)
    
''' [review]
Well-Known Floyd-Warshall
'''