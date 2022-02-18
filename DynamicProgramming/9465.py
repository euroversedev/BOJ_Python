import sys

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    array = [list(map(int, sys.stdin.readline().strip().split()))
            for _ in range(2)]

    if N > 1:
        array[0][1] += array[1][0]
        array[1][1] += array[0][0]
        
        for j in range(2, N):    # 모든 열
            for i in range(2):    # 모든 행
                array[i][j] += max(array[(i+1)%2][j-1],
                                   array[(i+1)%2][j-2])

    print(max(array[0][-1], array[1][-1]))