factorial = [0, 1] + [0] * 99
for i in range(2, 101):
    factorial[i] = factorial[i-1]*i
N, M = map(int, input().split())
print(factorial[N]//factorial[N-M]//factorial[M])
