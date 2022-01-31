N = int(input())
parent = list(map(int, input().split()))
K = int(input())    # 지울 노드의 번호 K
is_leaf = [True] * N

def solution(parent_num):
    parent[parent_num] = -2
    for i in range(N):
        if parent[i] == parent_num:
            parent[i] = -2
            solution(i)
        
solution(K)

for i in range(N):
    if parent[i] == -2:
        is_leaf[i] = False
    
    if -1 < parent[i]:
        is_leaf[parent[i]] = False

print(sum(is_leaf))