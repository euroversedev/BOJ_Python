N = int(input())
table = [[0] * (N+1) for _ in range(N+1)]    # 학생 
happy = [[0] * (N+1) for _ in range(N+1)]    # 만족도

for _ in range(N**2):
    array = list(map(int, input().split()))
    me = array[0]
    they = array[1:]
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if table[i][j] in they: 
                
            table[i][j]