import sys
sys.setrecursionlimit(10**4)

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

len_T = len(T)

def dfs(S, len_S):
    if S == T:
        return True
    
    if len_S > len_T:
        return False
    
    return dfs(S+'A', len_S+1) or dfs(S[::-1]+'B', len_S+1)

print(1 if dfs(S, len(S)) else 0)