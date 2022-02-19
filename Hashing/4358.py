import sys

dic = {}
total = 0
while True:
    try:
        name = sys.stdin.readline().strip()
        
        if name == "":
            break
        
        dic[name] = dic.get(name, 0) + 1
        total += 1
        
    except:
        break

for name, cnt in sorted(list(dic.items()), key = lambda x:x[0]):
    print("%s %.4f" % (name, (cnt/total*100)))


''' [review]
종료 조건을 찾지 못하는 경우 => EOF

sys.stdin.readline()은 빈 문자열을 반환하므로
위와 같이 반복문 탈출 가능.

++ round는 작동 방식이 특이하니까
그냥 저렇게 쓰자. 알아서 반올림해준다.
'''