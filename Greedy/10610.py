N = list(input())
N.sort()

if N[0] == str(0) and sum(map(int, N[1:])) % 3 ==0:
    print(''.join(N[::-1]))
else:
    print(-1)