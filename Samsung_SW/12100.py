from collections import deque
N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

result = 0
def move_left(array):
    array2 = [[0] * N for _ in range(N)]
    for i in range(N):
        q = deque()
        for j in range(N):
            if array[i][j] != 0:
                q.append(array[i][j])
        k = 0
        while q:
            a, b= 0, 0
            if q : a = q.popleft()
            if q : b = q.popleft()
            
            if a == b and a != 0:                
                array2[i][k] = a + b
                k += 1
            else:
                array2[i][k] = a
                k += 1
                if k < N:
                    array2[i][k] = b
                    k += 1
    return array2

def move_right(array):
    array2 = [[0] * N for _ in range(N)]
    for i in range(N):
        q = deque()
        for j in range(N-1, -1, -1):
            if array[i][j] != 0:
                q.append(array[i][j])
        k = N-1
        while q:
            a, b= 0, 0
            if q : a = q.popleft()
            if q : b = q.popleft()
            array2[i][k] = a + b
            k -= 1
    return array2

def move_up(array):
    array2 = [[0] * N for _ in range(N)]
    for i in range(N):
        q = deque()
        for j in range(N):
            if array[j][i] != 0:
                q.append(array[j][i])
        k = 0
        while q:
            a, b= 0, 0
            if q : a = q.popleft()
            if q : b = q.popleft()
            array2[k][i] = a + b
            k += 1
    return array2

def move_down(array):
    array2 = [[0] * N for _ in range(N)]
    for i in range(N):
        q = deque()
        for j in range(N-1, -1, -1):
            if array[j][i] != 0:
                q.append(array[j][i])
        k = N-1
        while q:
            a, b= 0, 0
            if q : a = q.popleft()
            if q : b = q.popleft()
            array2[k][i] = a + b
            k -= 1
    return array2


result = move_left(array)

print(result)

''' [review]
2차원리스트 복제를 위해서는 deepcopy를 사용해야 함.
'''
