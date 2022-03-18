import sys

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    
    code_array =[]
    secret_code = []
    # 암호화된 문자열들이 주어지면, 해시
    for _ in range(N+1):    # +1을 했기때문에 마지막에는 aboringsample에 대한 해시가 저장됨
        s = list(sys.stdin.readline().strip())
        code_array.append(s)
        
        i = 0
        alphabet = [-1] * 26     # 해당 알파벳의 포함 여부를 저장   
        tmp = []
        for ch in s:
            idx = ord(ch)-ord('a')
            if alphabet[idx] == -1:
                alphabet[idx] = i
                i += 1
            
            tmp.append(alphabet[idx])
        
        secret_code.append(tmp)
    
    # 해독문과 같은 해시를 가진 암호문을 찾아냄.
    dic = dict()
    flag = True
    for i in range(len(secret_code)-1):
        if secret_code[-1] == secret_code[i]:
            flag = False
            
            for j in range(len(secret_code[-1])):
                if code_array[i][j] in dic and dic[code_array[i][j]] != code_array[-1][j]:
                    dic[code_array[i][j]] = '?'
                else: dic[code_array[i][j]] = code_array[-1][j]
                    


    
    answer = []
    new_secret_code = list(sys.stdin.readline().strip())
    
                
    if flag:
        print("IMPOSSIBLE")
        continue
    
    
    for i in range(len(new_secret_code)):
        if new_secret_code[i] in dic and len(dic[new_secret_code[i]]) == 1:

            if list(dic.values()).count(dic[new_secret_code[i]]) > 1:
                answer.append('?')
                continue
                
            answer.append(dic[new_secret_code[i][0]])
        else:
            answer.append('?')
            
    print(''.join(answer))
    
        