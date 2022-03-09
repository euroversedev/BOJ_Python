import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
array = list(zip(range(1, N+1), array))

NGW = [0] * (N+1)
stack = [(0, 10**9)]
for idx, height in array[::-1]:
    # 나보다 작은 것들은 모두 나한테 신호를 보냄
    while stack and stack[-1][1] < height:
        idx_last, height_last = stack.pop()
        NGW[idx_last] = idx
    
    else:
        stack.append((idx, height))
print(*NGW[1:])
        

