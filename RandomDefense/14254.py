import sys
from collections import Counter


S = list(sys.stdin.readline().strip())
K = int(input())

len_S = len(S)

cnt = 0
for i in range(len_S-K):
    tmp = []
    for j in range(i, len_S, len_S-K):
        tmp.append(S[j])
    
    counter = Counter(tmp)
    cnt += len(tmp) - counter.most_common()[0][1]
    
print(cnt)


'''
amamamama
amavckdkz

am avckd
   avckd kz

9-7 2개   
av avckd
   avckd kz
    
A v A v A k A k A
  B   B   B   B

a a c d z => cdz를 교체
v v k k => vv혹은 kk를 교체
    
am amam

am amckz

am amama ma
'''

    

    