import sys

N, K = map(int, sys.stdin.readline().strip().split())
values = [int(sys.stdin.readline().strip()) for _ in range(N)]

result = 0
for value in values[::-1]:
    if K // value > 0:
        result += K // value
        K -= value * (K//value)
    if K == 0:
        break
print(result)

''' [review]
I+1번째 값이 I번째의 배수라는 조건에 집중
조건 빠짐없이 다 읽도록 연습하자.
'''