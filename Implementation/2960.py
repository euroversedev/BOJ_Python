import sys

N, K = map(int, sys.stdin.readline().strip().split())

# 초기에는 모든 수가 소수
isPrime = [True] * (N+1)

cnt = 0
for i in range(2, N+1):
    
    for j in range(i,N+1, i):
        if isPrime[j] == True:
            isPrime[j] = False
            cnt += 1
            
            if cnt == K:
                print(j)
                exit()
    