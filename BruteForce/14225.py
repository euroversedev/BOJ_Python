import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))

set_ = set([0])
for num in array:
    new_elem = []
    for elem in set_:
        new_elem.append(elem+num)
    set_.update(new_elem)
    
for i in range(1, sum(array)+2):
    if i not in set_:
        print(i)
        break