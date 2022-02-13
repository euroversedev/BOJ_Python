X, Y = map(int, input().split())
Z = round(Y/X)

def binary_search(start, end, Z):
    
    mid = (start+end) // 2
    K = round((Y+mid)/(X+mid))
    
    if start > end:
        if K == Z:        # 게임수를 늘려도 승률 변화X
            return Non
            
    if K == Z+1:
        return mid
    
    elif K < Z+1:
        return binary_search(mid+1, end)
    
    elif K > Z+1:
        return binary_search(start, mid-1)
        
result = binary_search(1, 10**9)
if result == None:
    print(-1)
else: print(result)