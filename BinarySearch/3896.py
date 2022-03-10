import sys
from bisect import bisect_left, bisect_right

'''K의 왼쪽과 오른쪽 소수를 찾아내면, 그 차이가 수열의 길이임.''' 

# 소수 리스트 구하기
isPrime = [False, False] + [True]* 1300000
for i in range(2, int(1300000**0.5)+1):
    if isPrime[i] == True:
        for j in range(2*i, 1300000, i):
            isPrime[j] = False    
prime = [x for x in range(2, 1300000) if isPrime[x]]

# 각 테케마다 수열의 길이 출력0
T = int(input())
for _ in range(T):
    K = int(sys.stdin.readline().strip())
    if isPrime[K] == True or K < 2:
        print(0)
        continue
    
    # K의 왼쪽과 오른쪽 소수를 찾아내면, 그 차이가 수열의 길이임.
    # prime[left]는 K보다 크거나 같은 소수임
    left = bisect_left(prime, K)
    

    print(prime[left]-prime[left-1])
    