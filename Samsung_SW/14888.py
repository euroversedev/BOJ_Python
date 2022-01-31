from itertools import permutations

N = int(input())
array = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

operator = ['+']*add + ['-']*sub + ['*']*mul + ['//']*div
opers = list(permutations(operator, N-1))

opers = set(opers)
max = -1 * int(1e9)
min = int(1e9)

for oper in opers:
    result = array[0]
    k = 1
    for op in oper:
        if op == '+':
            result += array[k]
        if op == '-':
            result -= array[k]
        if op == '*':
            result *= array[k]
        if op == '//':
            if result < 0:
                result = -1 * ((-1 * result) // array[k])
            else: result //= array[k]    
        k += 1
    if result > max : max = result
    if result < min : min = result



print(max)
print(min)
    
''' [review]
- 아래와 같이 eval 함수를 이용해서 문자열을 쉽게 계산할 수도 있지만,
- 해당 문제에서는 사칙연산 우선순위가 무조건 문자열 앞쪽부터라서 안됨.
s = []
    for j in range(N-1):
        s.append(str(array[j]))
        s.append(oper[i][j])
    s.append(str(array[-1]))
    
    print(''.join(s) + '=' + str(eval(''.join(s))))
'''
