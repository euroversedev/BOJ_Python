N = int(input())

a = N // 5
for i in range(a,-1,-1):
    b = (N-5*i) // 2
    for j in range(b,-1,-1):
        if i*5+j*2 == N:
            print(i+j)
            exit()
        
        if i*5+j*2 < N:
            break
            
print(-1)