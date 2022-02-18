N, P, Q = map(int, input().split())

dic = dict()

def dfs(N, P, Q):
    if N == 1: return 2
    if N == 0: return 1
    
    if N in dic.keys():
        return dic[N]
    
    L = N // P
    R = N // Q
    
    dic[N] = dfs(L, P, Q) + dfs(R, P, Q)
    return dic[N]

print(dfs(N, P, Q))
