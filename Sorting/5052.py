import sys

T = int(input())
for _ in range(T):
    flag = True
    N = int(sys.stdin.readline().strip())
    book = [0] * N
    Max = 0
    for i in range(N):
        phone = int(sys.stdin.readline().strip())
        book[i] = phone
        if Max < phone: Max = phone
    
    array = [0] * (Max+1)
    for i in range(N):
        num = book[i]
        while num > 0:
            array[num] += 1
            num = num//10
    
    for i in range(N):
        num = book[i]
        if array[num] > 1:
            flag = False
    
    if flag:
        print("YES")
    else:
        print("NO")