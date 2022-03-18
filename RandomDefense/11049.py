import sys

N = int(input())

array = []
for i in range(N):
    if i == 0:
        array = list(map(int, sys.stdin.readline().strip().split()))
    else: array.append(list(map(int, sys.stdin.readline().strip().split()))[1])

answer = 0
len_array = N + 1
while len_array > 2:
    # 최소가 되는 곱 연산을 매 반복마다 찾음 => 그리디
    print(array)
    
    min_ = (10**9, -1)
    for i in range(len_array-2):
        mul = array[i]*array[i+1]*array[i+2]
        if min_[0] > mul:
            min_ = (mul, i+1)
    
    del array[min_[1]]
    answer += min_[0]
    len_array -= 1
    print(answer)
print(answer)
    
    