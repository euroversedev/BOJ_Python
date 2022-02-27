import sys


G = int(input())
gate = [0] * (G+1)

P = int(input())
array = [int(sys.stdin.readline().strip()) for _ in range(P)]

for i in array:
    idx = bisect_left(gate, i)
    print(idx, flag[idx])
    if idx == 1 and flag[idx] == True:
        break
    
    if flag[idx] == True:
        flag[idx-1] = True
        gate[idx-1] = i
    
    if flag[idx] == False:
        flag[i] = True
print(gate)     
print(flag)     
print(sum(flag))

''' review
이분 탐색은 정렬된 데이터에서만 사용가능...
이 문제처럼 뒤죽박죽이면 쓰지 말자.

'''