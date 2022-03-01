from itertools import combinations

S = input()


stack = []
result = []
for idx, ch in enumerate(S):
    if ch == '(':
        stack.append((idx, ch))
        
    if ch == ')':
        idx2, _ = stack.pop()
        result.append((idx2, idx))

tmp = []
for len_ in range(1, len(result)+1):
    combis = combinations(result, len_)
    for combi in combis:
        tm = []
        for a, b in combi:
            tm.append(a)
            tm.append(b)
        tmp.append(tm)
    
answer = set()
for list_ in tmp:
    s = list(S)
    for idx in sorted(list_, reverse=True):
        s.pop(idx)
    answer.add((''.join(s)))
    
print(*sorted(answer), sep='\n')