from itertools import permutations
N, M = map(int, input().split())

array = [i for i in range(1, N+1)]
set_ = set(array)
perms = list(permutations(set_, M))

for perm in perms:
    print(' '.join(str(num) for num in perm))
    # == print(' '.join(map(str, perm)))

''' [review]
1. permutaions와 combinations의 반환 값은
제네레이터라서 인덱싱으로 처리가 불가하다.

2. join에 str(perm)을 통째로 넣을 경우
[ 1 , 2 ]와 같이 괄호까지 같이 들어가 버린다.
숫자만 골라서 넣어주려면 위와 같이 하자.

3. array와 set_을 따로 만들 필요없이,
permutations(range(1, N+1), M)과 같이 처리도 가능함.

++ 백트래킹이란?
일명 "가지치기", 가능성이 없는 대상은 탐색에서 제외하여 효율적으로 답을 구함.
브루트포스와 유사하면서, 시간복잡도를 완화하는 그리디 느낌.
'''

