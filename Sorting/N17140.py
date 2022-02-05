import sys
from collections import Counter
import copy

# A[r-1][c-1]이 k가 되기 위한 연산 횟수 구하기
r, c, k = map(int, input().split())   

A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]
print(A)

# R 연산 : 행 >= 열
def func_R():
    global A
    max_len = 0
    
    for i in range(len(A)):    # 모든 행에 대해 연산
        row = A[i]
        count = Counter(row)
        li = sorted(count.most_common(), key = lambda x: x[1])
        print(li)
        new_row = []
        for i in range(len(li)):
            if li[i][0] == 0:
                continue
            
            new_row += [li[i][0]] + [li[i][1]]
        print(new_row)
        A[i] = new_row
        print(A[i])
        if len(row) > max_len: max_len = len(row)
        
    # 짧은 행에 0 패딩 추가, 길이가 100 이상이면 삭제
    for row in A:
        if len(row) < max_len:
            row += [0] * (max_len - len(row))
        
        if len(row) > 100:
            row = row[0:100]

# C 연산 : 행 < 열
def func_C():
    pass

cnt = 0
while True:
    print(A)
    if A[r-1][c-1] == k:
        break
    
    flag = True
    if len(A[0]) >= len(A):
        func_R()
        flag = False
    
    if flag:
        func_C()
    print(A)
    break
    cnt += 1

print(cnt)