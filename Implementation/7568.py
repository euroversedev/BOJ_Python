N = int(input())
array = [tuple(map(int, input().split())) for _ in range(N)]
rank = [0] * N

for i in range(N):
    cnt = 1
    for j in range(N):
        if i == j: continue    # 자기 자신은 pass
        
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            cnt += 1
        
        rank[i] = cnt 
print(' '.join(map(str, rank)))

''' [review]
join은 인자로 문자열이 와야 함.
아니면, 매 반복마다 해당 rank를 출력해주는 방법도 있음.
print(rank, end = " ")
'''