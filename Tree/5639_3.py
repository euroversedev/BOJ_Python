import sys
sys.setrecursionlimit(10**6)

array = []
while True:
    try:
        array.append(int(sys.stdin.readline().strip()))
    except:
        break

def go(start, end):
    # print(start, end)
    if start > end: return
    
    if start == end:
        print(array[start])
        return
    
    flag = start
    while flag <= end and array[flag] <= array[start]:
        flag += 1
    
    if start+1 <= flag-1:
        go(start+1, flag-1)
    
    if flag <= end:
        go(flag, end)
        
    print(array[start])
    
go(0, len(array)-1)