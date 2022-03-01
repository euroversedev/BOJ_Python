s = list(input())

result = []
for idx, ch in enumerate(s):
    if ch=='X':
        cnt = 0
        while len(s) > idx and s[idx] == 'X':
            s[idx]= ''
            cnt +=1
            idx += 1
        
        if cnt % 2 == 1:
            print(-1)
            exit()
            
        for _ in range(cnt//4, 0, -1):
            result.append("AAAA")
        for _ in range((cnt%4)//2, 0, -1):
            result.append("BB")
    
    if ch=='.':
        result.append('.')
        
print(''.join(result))

''' [review]
board = input()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if 'X' in board:
    print(-1)
else:
    print(board)
'''