import sys

N, H = map(int, sys.stdin.readline().strip().split())

A, B = [0] * (H+1), [0] * (H+1)
for _ in range(N//2):
    # 석순
    A[int(sys.stdin.readline().strip())] += 1
    
    # 종유석
    B[int(sys.stdin.readline().strip())] += 1

prefix_sum_A = [0] * (H+1)
prefix_sum_A[H] = A[H]
for h in range(H-1, 0, -1):
    prefix_sum_A[h] = prefix_sum_A[h+1] + A[h]

prefix_sum_B = [0] * (H+1)
prefix_sum_B[H] = B[H]
for h in range(H-1, 0, -1):
    prefix_sum_B[h] = prefix_sum_B[h+1] + B[h]
    
    
prefix_sum_AB = [0] * (H+1)
for h in range(1, H+1):
    prefix_sum_AB[h] = prefix_sum_A[h] + prefix_sum_B[H-h+1]

# print(prefix_sum_A)
# print(prefix_sum_B)
# print(prefix_sum_AB)

print(min(prefix_sum_AB[1:]), prefix_sum_AB[1:].count(min(prefix_sum_AB[1:])))

