import sys

N, S = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

end = 0
sum_ = 0
answer = 10**9
for start in range(N):
    while start <= end < N and sum_ < S:
        sum_ += array[end]
        end += 1

    if sum_ >= S:
        answer = min(answer, end-start)
            
    sum_ -= array[start]
    
print(answer if answer != 10**9 else 0)

'''
시작과 끝, 합은 모두 0에서 시작한다.
'''