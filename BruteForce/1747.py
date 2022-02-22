N = int(input())

# 소수 판별 함수
def func1(x):
    if x == 1: return False
    
    for i in range(2, int(x**0.5)+1):
        if i != x and x % i == 0: return False
    
    return True

# 팰린드롬판별 함수
def func2(x):
    tmp = list(str(x))
    if x == int(''.join(tmp[::-1])):
        return True
    else: return False

array = [False, False] + [True] * 1300030
for i in range(2,1300032):
    if array[i]:
        for j in range(2*i,1300032,i):
            array[j] = False


for num in range(N, 1003002):
    if array[num] and func2(num):
        print(num)
        break