P = [list(map(int, input().split())) for _ in range(3)]

def ccw(x1, y1, x2, y2, x3, y3):
    result = x1*y2 + x2*y3 + x3*y1 \
                - (x2*y1 + x3*y2 + x1*y3)
    return result

P = sum(P, [])
result = ccw(*P)

if result == 0:
    print(0)
elif result > 0:
    print(1)
else:
    print(-1)
    
''' [review]
2차원 리스트를 1차원 리스트로 변환하는 법
: list_1d = sum(list_2d, [])
(시스템 리소스를 많이 사용하여 추천하는 방식은 아님.)
sum(iterable, start)는 start에 iterable을 더하는 방식으로 작동함
sum(list, [])는 []+list[0]...과 같이 작동하여 1차원 리스트를 반환함.
'''