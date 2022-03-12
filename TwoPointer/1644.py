import sys
N = int(input())

# 소수 집합 구하기 (에라토스테네스의 체)
isPrime = [False, False] + [True] * (N-1)
for i in range(2, int(N**0.5)+1):
    if isPrime[i] == True:
        for j in range(2*i, N+1, i):
            isPrime[j] = False

prime_numbers = []
for idx, boolean in enumerate(isPrime):
    if boolean == True:
        prime_numbers.append(idx)

        
# N을 연속된 소수의 합으로 나타내는 경우의 수 구하기 (투 포인터)
start, end = 0, 0
sum_ = prime_numbers[0]
cnt = 0
while start <= end:
    if sum_ == N:    # 여기사 start를 옮겨야할지 end를 옮겨야할지 모르겠네
        cnt += 1
        end += 1
        sum_ += prime_numbers[end]
        continue
        
    if sum_ < N:
        end += 1
        sum_ += prime_numbers[end]
        continue
        
    if sum_ > N:
        sum_ -= prime_numbers[start]
        start += 1
        
print(cnt)
