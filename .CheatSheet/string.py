# 문자열 다룰때 어떤 문자열을 다른 문자열로 대체하고 싶을 때,
# 1343 폴리오미노 문제에서 다음과 같이 코딩 가능

board = input()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if 'X' in board:
    print(-1)
else:
    print(board)
    
    
    
# 문자열을 두개의 문자를 기준으로 쪼개야하는 경우, (20365번 문제)
# ex. AABAABBAA를 AA, B, AA, BB, AA로 쪼개야하는 경우 아래와 같이 코딩 가능

array = input()
a = array.split("A")
res1 = len(a) - a.count("") + 1
b = array.split("B")
res2 = len(b) - b.count("") + 1
print(min(res1, res2))