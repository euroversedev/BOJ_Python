import sys
sys.setrecursionlimit(10**9)

X = int(input())
tmp = [X]
result = []
min_len = 10**9
def dfs(X):
    global min_len, result
    
    if len(tmp) >= min_len:    # 이 코드의 핵심. 없으면 시간초과
        return
    
    if X == 1:
        result = tmp[:]
        min_len = len(tmp)
    
    if X%3==0:
        tmp.append(X//3)
        dfs(X//3)
        tmp.pop()
    
    if X%2==0:
        tmp.append(X//2)
        dfs(X//2)
        tmp.pop()
    
    if X-1 > 0:
        tmp.append(X-1)
        dfs(X-1)
        tmp.pop()

dfs(X)
print(min_len-1)
print(*result)

'''
dfs를 이용한 풀이 (일종의 백트래킹)
=> 위 코드로도 가능하지만,

항상 "최소경로"를 찾을 때에는 BFS를 이용하자.
or DP
'''