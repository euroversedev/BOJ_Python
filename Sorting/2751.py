import sys

N = int(input())
array =[0] * N
for i in range(N):
    array[i] = int(sys.stdin.readline().strip())
array.sort()
print(*array, sep='\n')

''' [review]
리스트를 한 줄씩 출력하는법
: (*) Unpacking Operator 사용
print(*array, sep="\n")
'''