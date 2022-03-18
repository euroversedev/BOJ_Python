import sys

N, M = map(int, sys.stdin.readline().strip().split())

parent = [i for i in range(N+1)]
boolean = [None] * (N+1)


# 진실을 아는 사람들
truth_num, *truth = map(int, sys.stdin.readline().strip().split())
for idx in truth:
    boolean[idx] = True
    
    
def find_parent(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a <= b: parent[b] = a
    else: parent[a] = b
    
answer = 0
tmps =[]
for _ in range(M):
    num, *tmp = map(int, sys.stdin.readline().strip().split())
    
    tmps.append(tmp)
    if num >= 2:
        for idx in range(1, len(tmp)):
            if find_parent(tmp[idx-1]) != find_parent(tmp[idx]):
                union_parent(tmp[idx-1], tmp[idx])

set_ = set(parent[1:])
for num in truth:
    set_.remove(parent[num])
    
person_ = []
for i in range(1, N):
    if parent[i] in set_:
        person_.append(i)

print(person_)

answer = 0
for tmp in tmps:
    flag = True
    
    for i in tmp:
        if i not in person_:
            flag = False
            break
            
    if flag: answer += 1
        
print(answer)