import sys

N = int(input())
distance = list(map(int, sys.stdin.readline().strip().split()))
price = list(map(int, sys.stdin.readline().strip().split()))

min_price = 10**10
result = 0
for idx, pri in enumerate(price[:-1]):

    if pri < min_price: min_price = pri
    result += distance[idx] * min_price
print(result)    