N, M = map(int, input().split())

stack = []
def dfs(x):
    if len(stack) == M:
        print(' '.join(stack))
        return
    
    for i in range(x, N+1):
        stack.append(str(i))
        dfs(i)
        stack.pop()
    
    return

dfs(1)

''' [review]
비내림차순 수열 => 중복 조합과 같다. (combinations_with_replacement)
'''
