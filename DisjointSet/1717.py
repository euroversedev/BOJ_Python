import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
parents = [i for i in range(N+1)]    # 초기에는 자기 자신이 부모

#def find_parent(x):
#    if parents[x] == x:    # 자기 자신이면 루트 노드라는 뜻
#        return x
#    else:
#        return find_parent(parents[x])    # 부모의 부모를 찾는 방법으로 재귀적으로 루트까지 올라감

    
def find_parent(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find_parent(parents[x])
        return parents[x]
    
def union_parent(x, y):
    # 더 작은 애가 부모가 됨.
    x = find_parent(x)
    y = find_parent(y)
    
    if x < y : parents[y] = x
    else: parents[x] = y

for _ in range(M):
    cmd, a, b = map(int, sys.stdin.readline().strip().split())
    
    if cmd == 0:
        union_parent(a,b)
        
    elif cmd == 1:
        result = find_parent(a) == find_parent(b)
        if result:
            print("YES")
        else: print("NO")
            
''' [review]
위에 find_parent처럼 코딩하면 매번 호출할때 마다 부모의 부모를 타고 올라가기 때문에
시간복잡도가 비효율 적임 => 부모의 부모를 타고 올라갈때, 다음과 같이 코딩하면 다음번 호출 때 시간 복잡도 낮암짐
def find_parent(x):
   if parents[x] == x:
       return x
    else:
        parents[x] = find_parent(parents[x])
        return parents[x]

'''