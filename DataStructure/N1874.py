import sys

N = int(input())
array = [int(sys.stdin.readline().strip()) for _ in range(N)]

seq = []
stack = []
i = 1
flag = True
for num in array:
    if (num not in stack) and (i <= num):
        for _ in range(num -i +1):
            stack.append(i)
            seq.append("+")
            i += 1

    
    if num in stack:
        while True:
            k = stack.pop()
            seq.append("-")
            if k == num:
                break
    
    else:
        flag = False
        break
        
if flag:
    print(*seq, sep='\n')
else:
    print("NO")
        
        