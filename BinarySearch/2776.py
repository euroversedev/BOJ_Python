import sys

T = int(input())
for _ in range(T):
    N = int(input())
    note_1 = list(map(int, sys.stdin.readline().strip().split()))
    dict_ = dict()
    for i in note_1:
        dict_[i] = True    
    
    M = int(input())
    note_2 = list(map(int, sys.stdin.readline().strip().split()))
    for i in note_2:
        if i in dict_.keys():
            print(1)
        else:
            print(0)