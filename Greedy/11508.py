import sys

N = int(input())
price = [int(sys.stdin.readline().strip()) for _ in range(N)]

price.sort(reverse=True)
for i in range(2,N//3*3,3):
    price[i] = 0

print(sum(price))