import sys

N, M = map(int, sys.stdin.readline().strip().split())
A = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

cnt = 0
for y in range(N-2):
    for x in range(M-2):
        if A[y][x] != B[y][x]:
            cnt += 1
            for dy in range(3):
                for dx in range(3):
                    A[y+dy][x+dx] = 1 if A[y+dy][x+dx]==0 else 0

                    
for y in range(N):
    for x in range(M):
        if A[y][x] != B[y][x]:
            print(-1)
            exit()
            
print(cnt)