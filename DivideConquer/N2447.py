N = int(input())

def pattern(N):
    if N == 1:
        print("*", end="")
        return
    
    k = (N-1)//3
    li_ = [(0, k+1), (k+2, 2*k+2), (2*k+3, N-1)]
    
    for startY, endY in li_:
        for startX, endX in li_:
            if (startX, endX) == li_[1] and (startY, endY) == li_[1]:
                print("9"*(N//3), end="")
            else:
                pattern(N//3)
        print()


pattern(N)

# 세로 : 0부터 N-1까지 => 앞 0~(N-1)/3까지 + 가운데 (N-1)/3 +1부터 (N-1)/3*2 +1까지 + 뒤 (N-1)/3*2 +2부터 N-1까