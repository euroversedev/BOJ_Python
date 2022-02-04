D, K = map(int, input().split())

array = [(1,0), (0,1), (1,1)]
for _ in range(3, D):
    array.append((array[-1][0]+array[-2][0], array[-1][1]+array[-2][1]))
x = array[-1][0]
y = array[-1][1]

breaker = False
for i in range(K//x):
    for j in range(K//y):
        if x*i + y*j == K:
            print(i)
            print(j)
            breaker = True
            break
    if breaker == True:
        break
        