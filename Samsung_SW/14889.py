import sys
from itertools import combinations

N = int(input())
stat = [list(map(int, sys.stdin.readline().strip().split()))
       for _ in range(N)]

MIN = 10**9
combis = combinations(range(N), N//2)
teams = []
for combi in combis:
    teams.append(combi)

for combi in teams[:len(teams)//2]:
    groupA = 0
    groupB = 0
    
    for i in range(N):
        for j in range(N):
            if (i in combi) and (j in combi):
                groupA += stat[i][j] + stat[j][i]
            elif (i not in combi) and (j not in combi):
                groupB += stat[i][j] + stat[j][i]
                
    result = abs(groupA - groupB)

    if result < MIN:
        MIN = result
        
print(MIN//2)

''' [review]
시간 초과 나옴.
=> 위와 같이 이중 포문으로 모든 stat을 검사하는 것은 너무 많은 시간 소요.
=> 조합을 기준으로 원소들의 stat을 가져오도록 구현해보자 => 14889_2.py
'''