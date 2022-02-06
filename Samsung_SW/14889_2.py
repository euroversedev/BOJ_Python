import sys
from itertools import combinations, permutations

N = int(input())
stat = [list(map(int, sys.stdin.readline().strip().split()))
       for _ in range(N)]

MIN = 10**9
combis = combinations(range(N), N//2)
teams = []
for combi in combis:
    teams.append(combi)

for i in range(len(teams)//2):
    groupA = 0
    groupB = 0
    
    for j in teams[i]:
        for k in teams[i]:
            groupA += stat[j][k]
    
    for j in teams[-1-i]:
        for k in teams[-1-i]:
            groupB += stat[j][k]
    
    result = abs(groupA - groupB)

    if result < MIN:
        MIN = result
        
print(MIN)

''' [review]
문제 조건 안에서
시간 복잡도를 낮출 수 있도록 코딩하는 연습을 하자.

두 집합으로 나눌때
combis[0]과 combis[-1]은 서로소 관계이다.
따라서 반갈하면 됨.

이 문제는 백트래킹 알고리즘으로 분류되는데,
조합 구하는 것을 백트래킹으로 볼 수도 있고,
팀에 속한 인원 == N//2를 만족하면 각 팀의 stat 합을 구하는 방식으로
백트래킹으로 볼 수도 있음.
'''
