import sys

N = int(input())

answer = 1
sum_x = int(sys.stdin.readline().strip())
for i in range(2, N+1):
    x = int(sys.stdin.readline().strip())
    answer *= ((i-1)*x-sum_x) % 1000000007
    sum_x += x
    
    print(answer, sum_x)
    
print(answer)
    