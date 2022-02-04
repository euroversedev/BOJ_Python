import sys

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    array = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    array.sort()
    
    cnt = 0    # 뽑지 않는 인원
    MIN = array[0][1]
    for i in range(1, n):
        if array[i][1] > MIN:
            cnt += 1
        else:
            MIN = array[i][1]
    print(n-cnt)