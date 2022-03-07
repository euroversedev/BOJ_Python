N = int(input())

cnt = 0
for i in range(317,0,-1):
    if N == 0: break
        
    if N >= i**2 :
        cnt += N // (i**2)
        N = N % (i**2)

print(cnt)
