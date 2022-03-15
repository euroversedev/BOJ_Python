import sys

N = int(input())
array = sorted(map(int, sys.stdin.readline().strip().split()))

min_answer = 10**9
answer = ()

for i in range(N-2):

    sum_ = array[i]
    
    # two pointer
    end = i+2
    for start in range(i+1, N):
        sum_ += array[start]
        
        while start < end and end < N:
            
            
            
            sum_ += array[end]
            print(i, start, end, abs(sum_))
            
            if abs(sum_) < min_answer:
                min_answer = abs(sum_)
                answer = (array[i], array[start], array[end])
                
            else:
                sum_ -= array[end]
                break
                
            sum_ -= array[end]
            end += 1
        
        sum_ -= array[start]

print(answer)