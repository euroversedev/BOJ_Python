from itertools import product

N, K = map(int, input().split())

products = product(range(N+1), repeat=K)

cnt = 0
for p in products:
    sum_ = 0
    for i in p:
        sum_ += i
        if sum_ > N:
            break
    if sum_ == N:
        cnt += 1
        
print(cnt)