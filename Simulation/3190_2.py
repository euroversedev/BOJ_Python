import sys
from collections import deque

def func(a):
    return int(a)-1

N = int(input())
K = int(input())
apples = [tuple(map(func, sys.stdin.readline().strip().split()))\
         for _ in range(K)]
L = int(input())
move = [tuple(sys.stdin.readline().strip().split())\
         for _ in range(L)]

# 뱀의 위치
snake = deque()
snake.append([0,0])

time = 0
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0
while True:
    for i in range(len(move)):
        if time == int(move[i][0]):
            if move[i][1] == 'D':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
                
    dy, dx = d[direction]
                
    if not (0<=snake[-1][0]+dy<N and 0<=snake[-1][1]+dx<N):   # 벽
        break
    
    if ([snake[-1][0]+dy, snake[-1][1]+dx]) in snake:
        break
    
    snake.append([snake[-1][0]+dy, snake[-1][1]+dx])
    if (snake[-1][0], snake[-1][1]) not in apples:
        snake.popleft()
        
    else:
        for i in range(len(apples)):
            if (snake[-1][0], snake[-1][1]) == apples[i]:
                apples[i] = (N, N)
    
    time += 1

print(time+1)
    
''' [review]
기존에는 보드에 지렁이가 존재하는 위치를 1로 표시했으나,
이동과 삭제에 어려움을 겪음.

=>
지렁이는 헤드와 테일의 이동과 삭제를 용이하게 하려면
큐 자료구조로 위치를 저장하는게 좋겠는데?

++ 큐 구현은 기본적으로 데크로 하기때문에,
pop 뿐만아니라 append도 left에서 가능함.
ex. snake.appendleft()

++ move와 같이 시간별로 순서대로 들어오는 애들은
for문으로 돌릴필요없이 큐에 담아서
move[0]만 확인하고, 필요시엔 popleft()하면 됨.
'''