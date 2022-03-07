X, Y = map(int, input().split())
Z = int(Y*100/X)

def binary_search(start, end):
    mid = (start+end)//2
    
    if start >= end:
        return start
    
    # Z가 상승한다면, 더 적은 게임을 해도 됨.
    if int((mid+Y)*100/(mid+X)) > Z:
        return binary_search(start, mid)
        
    else:
        return binary_search(mid+1, end)

result = binary_search(1, X)
if Z>=99:
    print(-1)
else:
    print(result)
 