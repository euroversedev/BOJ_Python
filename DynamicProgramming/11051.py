N, K = map(int, input().split())

fac = [1] * (N+1)
for i in range(1, N+1):
    fac[i] = (fac[i-1] * i) % 10007

print(fac[N] // fac[N-K] // fac[K])