S1 = input()
S2 = input()

# dp에 ZeroPadding을 추가하기 위해 (길이+1)
# -> 연산 시에 범위 밖으로 나가는 것을 예외처리 해주지 않아도 됨.
dp = [[0] * (len(S2)+1) for _ in range(len(S1)+1)]

for y in range(1, len(S1)+1):
    for x in range(1, len(S2)+1):
        
        # 최근에 추가한 글자가 서로 같을 때
        # ZeroPadding 추가한 것을 고려하여 인덱스-1을 비교
        if S1[y-1]==S2[x-1]:
            dp[y][x] = dp[y-1][x-1] + 1
            
        # 최근에 추가한 글자가 서로 다를 때
        else:
            dp[y][x] = max(dp[y][x-1], dp[y-1][x])

            
result = []
for i in range(1, len(S2)+1):
    if dp[-1][i] != dp[-1][i-1]:
        result.append(S2[i-1])

print(*dp, sep='\n')
if result: print(''.join(result))