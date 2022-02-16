import sys

N = int(input())
matrix = [list(map(int, sys.stdin.readline().strip().split()))
         for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = 1

for row in matrix:
    print(*row)

''' [review]
N의 크기가 작고, 모든 정점에서 다른 모든 정점에 대한
정보를 찾는 법 => 플로이드 워셜 알고리즘
'''