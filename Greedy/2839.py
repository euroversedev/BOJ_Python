N = int(input())
i, j = 0, 0

def dfs(sum_, i, j):
    if sum_ == N:
        return i + j
    
    elif sum_ > N:
        return 10**9
    
    else:
        a = dfs(sum_+5, i+1, j)
        b = dfs(sum_+3, i, j+1)
        result = min(a, b)
        return result
    
result = dfs(0, 0, 0)
if result == 10**9:
    print(-1)
else:
    print(result)
    
''' [review]
N이 커서 dfs로 풀면 재귀가 너무 깊게 쌓이고 시간초과 남
=> 2839_2.py
'''