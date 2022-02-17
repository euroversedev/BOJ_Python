import sys
sys.setrecursionlimit(10**9)
''' dfs를 이용한 풀이 '''

N = int(input())
def make_one(X):
    if X==1:
        return 1 
    
    tmp = [make_one(X-1)]
    if X%3==0:
        tmp.append(make_one(X//3))
        
    if X%2==0:
        tmp.append(make_one(X//2))
    
    return min(tmp)+1

print(make_one(N)-1)

''' [review]
해당 풀이는 메모리 초과가 남.
문제 풀다가 dfs 로 풀 수 있을 거란 생각이 들 떄
"혹시 같은 케이스를 반복해서 호출하지는 않는지 의심하자"
이런 경우에는 메모이제이션을 이용한 DP가 훨씬 유리하다.
'''