from itertools import combinations

N, M = map(int, input().split())
combis = combinations(range(1, N+1), M)
for combi in combis:
    print(' '.join(map(str, combi)))

''' [review]
해당 문제에는 적합한 풀이지만,
백트래킹과는 거리가 조금 있다.

백트래킹으로 풀려면 dfs(or 재귀)를 이용해서 가지치기로 풀어야 함.
ex. 
def dfs(start):
    if len(stack)== m:
        print(*stack)
        return
    
    for i in range(start,n+1):
        if i not in stack:
            stack.append(i)
            dfs(i+1)        
            temp = stack.pop()
        
dfs(1)
'''