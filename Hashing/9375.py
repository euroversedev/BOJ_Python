import sys

T = int(input())
for _ in range(T):
    dic = dict()
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        name, category = sys.stdin.readline().strip().split()
        if category not in dic.keys():
            dic[category] = [name]
        else:
            dic[category].append(name)
    
    result = 1
    for category in dic.keys():
        len_ = len(dic[category])
        result *= (len_+1)
        
    print(result - 1)