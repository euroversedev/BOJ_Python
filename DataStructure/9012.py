import sys

N = int(input())

for _ in range(N):
    stack = []
    s = list(sys.stdin.readline().strip())
    flag = True
    for i in range(len(s)):
        if s[i] == '(' :
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                flag = False
        else:
            pass

    
    if len(stack) > 0 or flag == False:
        print("NO")
    else:
        print("YES")