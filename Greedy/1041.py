import sys

N = int(input())
dice = [0] + list(map(int, sys.stdin.readline().strip().split()))



# 1면이 보이는 최솟값
one_ = min(dice[1:])

# 2면이 보이는 최솟값
two_ = 10**9
for i in range(1,7):
    for j in range(1,7):
        if i + j != 7 and i != j:
            two_ = min(two_, dice[i] + dice[j])

# 3면이 보이는 최솟값
three_ = 10**9
for x, y, z in [(1, 2, 3), (1,3,5),(1,5,4),(1,4,2),(6,2,3),(6,3,5),(6,5,4),(6,4,2)]:
    three_ = min(three_, dice[x]+dice[y]+dice[z])

if N  == 1:
    print(sum(sorted(dice)[:6]))
else:
    result = 4*three_ + (8*(N-2)+4)*two_ + (5*(N**2)-12-(16*(N-2)+8))*one_
    print(result)