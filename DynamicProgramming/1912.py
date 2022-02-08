import sys

N = int(input())
seq = list(map(int, sys.stdin.readline().strip().split()))
prefix_sum = [0] * len(seq)
prefix_sum[0] = seq[0]
for i in range(1, len(prefix_sum)):
    prefix_sum[i] = prefix_sum[i-1] + seq[i]

    
sorted_sum = sorted(enumerate(prefix_sum), key = lambda x: (x[1], x[0]))

breaker = False
for idxB, bigger in sorted_sum[::-1]:
    for idxS, smaller in sorted_sum:
        if idxS < idxB:
            print(bigger-smaller)
            breaker = True
            break
        
    if breaker:
        break
        
    

        
''' [review]
prefix_sum을 구하고 부분 수열의 합의 최대를 구하려고 봤더니
이중반복으로 그 갭을 모두 구해야할거같네.. N이 커서 안되는데
그러면, prefix_sum을 sort한 다음에 양끝에서 투포인터 써야겠다.=> 실패

DP에 너무 몰입한 나머지
DP배열을 만드는 풀이과정 외에 다른 방법을 떠올리지 못했다.
해당 문제는 단순히 수열의 처음부터 훑어나가며 최대합을 갱신할 수 있다. => 1912_2.py

=> DP로 푸는 방법도 물론 존재한다. 내가 떠올리지 못했을 뿐
dp[i] = max(array[i], array[i]+dp[i-1])
'''