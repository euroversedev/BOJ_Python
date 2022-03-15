target = int(input())

NUM = "0"
cnt = -1
while True:
    
    if int(NUM) > 9876543210:
        print(-1)
        exit()
    
    
    flag = True
    for i in range(1, len(NUM)):
        if NUM[i-1] > NUM[i]:
            continue
        else:
            flag = False
            break
    
    if flag:
        cnt += 1
        
        if cnt == target:
            print(NUM)
            exit()
        NUM = str(int(NUM)+1)
        
        
    else:
        NUM = str(((int(NUM)//(10**(len(NUM)-i)))+1)*(10**(len(NUM)-i)))
    

    
    