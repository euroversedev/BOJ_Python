N = int(input())
M = int(input())
if M == 0:
    broken_button = [-1]
else:
    broken_button = list(map(int, input().split()))

    
btn = [True] * 10
for i in range(10):
    if i in broken_button: btn[i] = False



a, b = N-1, N+1
while True:
    a += 1
    b -= 1
    
    
    flag = True
    for num in list(map(int, str(a))):
        if btn[num] == False:    # 고장난 버튼의 수가 포함된 경우
            flag = False
            break
            
    if flag:
        break
    
    if b >= 0:
        flag2 = True
        for num in list(map(int, str(b))):
            if btn[num] == False:    # 고장난 버튼의 수가 포함된 경우
                flag2 = False
                break
    
        if flag2:
            break
    else:
        break
    
result = a if min(a-N, N-b)==a-N else b
if abs(result-N) > abs(100-N):
    print(abs(100-N))
else:
    
    print(result-N + len(str(result)))
    
    
''' [review]
    for num in list(map(int, str(b))):
ValueError: invalid literal for int() with base 10: '-'
=> str(b)를 정수형으로 형변환하려는데 '-'기호가 있어서 발생한다.
( 음수가 발생하는 케이스를 제외시켜 줘야 함. )


'''