import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))

NGE = [-1] * N
stack = [(array[0], 0)]
for idx, num in enumerate(array[1:]):
    
    while stack and num > stack[-1][0]:
        _, idx2 = stack.pop()
        NGE[idx2] = num
    
    stack.append((num, idx+1))

print(*NGE)

''' [review]
"나보다 큰게 나타날 때 까지 스택에 저장한다"

타워였나 그 문제랑 비슷한듯.

자료구조 빈출유형임.
'''