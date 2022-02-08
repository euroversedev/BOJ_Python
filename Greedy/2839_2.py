N = int(input())
kg_5 = N // 5
kg_3 = N // 3

result = 10**9
for i in range(kg_5, -1, -1):
    for j in range(0, kg_3 +1):
        if i*5 + j*3 == N:
            result = min(result, i+j)

if result == 10**9:
    print(-1)
else:
    print(result)