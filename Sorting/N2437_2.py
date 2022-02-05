import sys
N = int(input())

# 저울추의 무게 정보
array = list(map(int, sys.stdin.readline().split()))
array.sort()

# 가능한 무게
positive_w = set()
for weight in array:
    add_li = []
    for w in positive_w:
        add_li.append(w+weight)
    add_li.append(weight)
    
    positive_w.update(add_li)

for i in range(1 ,sum(array)):
    if i not in positive_w:
        print(i)
        break
