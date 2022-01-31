array = [list(map(int, input())) for _ in range(4)]
K = int(input())    # K번 회전
  
def rotate(num, direction, visited):

    #print(*array, sep='\n')
    #print()
    if not (0<=num<4) or visited[num]==True : return
    visited[num] = True
    left = array[num][6]
    right = array[num][2]
    
    if direction == 1:    # 시계방향
        array[num] = [array[num][-1]] + array[num][0:-1]
    elif direction == -1: # 반시계방향
        array[num] = array[num][1:] + [array[num][0]]
    
    if num-1 >= 0:
        if array[num-1][2] != left:
            rotate(num-1, -1*direction, visited)
    if num+1 < 4:
        if array[num+1][6] != right:
            rotate(num+1, -1*direction, visited)
        
for _ in range(K):
    visited = [False] * 4
    num, direction = map(int, input().split())
    rotate(num-1, direction, visited)

result = 0
score = [1, 2, 4, 8]
for i in range(4):
    if array[i][0] == 1:
        result += score[i]


print(result)

''' [review]
array[num] = [array[num][-1]] + array[num][0:-2]에서
리스트를 +로 붙여할 때, 각 항들은 모두 리스트여야한다.
=> array[num][-1]은 정수형 원소 하나라서 [ ]로 감싸주어야 한다.

@ visited 없이 재귀문을 짜면 3번 => 2번과 4번 => (1번과 3번)과 3번 ...
이렇게 같은 번호를 여러번 방문하게 됨.

'''