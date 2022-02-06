N, M = map(int, input().split())

stack = []
def dfs():
    if len(stack) == M:
        print(' '.join(stack))
        return
    
    for i in range(1, N+1):
        stack.append(str(i))
        dfs()
        stack.pop()
    
    return

dfs()

''' [review]
이 문제는 중복 순열을 이용해서 풀 수도 있음

중복 순열: product(iterable, repeat = num)
ex. A = [1,2,3]에서 중복을 허용하여 길이 2의 순열 만들기
    product(A, repeat = 2)
    
중복 조합: combinations_with_replacement(iterable, num)
ex. A = [1,2,3]에서 중복을 허용하여 길이 2의 조합 만들기
    combinations_with_replacement(A, 2)
    
★ 출력할 때
print(*stack, sep=' ')보다
print(' '.join(map(str, stack)))가 빠르다.

++ stack.append(str(i))로 미리 문자열로 넣어주어
print(' '.join(stack))으로 하면 훨씬 빠르다.
'''


