import sys

T = int(input())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    A = sorted(list(map(int, sys.stdin.readline().strip().split())))
    B = list(map(int, sys.stdin.readline().strip().split()))
    
    # b보다 큰 A의 갯수를 찾으면 됨.
    cnt = 0
    for b in B:
        start, end = 0, N-1
        while start <= end:
            mid = (start+end)//2
            
            if A[mid] > b:
                end = mid -1
            
            if A[mid] <= b:
                start = mid +1
            
        cnt += N-start
    print(cnt)