import sys

dic = dict()
N, M = map(int, input().split())
for i in range(1, N+1):
    dic[sys.stdin.readline().strip()] = i
    
dic_reversed = dict(map(reversed, dic.items()))
for _ in range(M):
    s = sys.stdin.readline().strip()
    keyList = dic.keys()
    if s in keyList:
        print(dic[s])
        
    else:
        print(dic_reversed[int(s)])
        
''' [review]
영어랑 숫자 구분하는 법
=> if s.isalpha():

map으로 reversed하지 않고
따로 dic2만들어서 반복문으로 dic입력 받을 때 같이 처리해도 됨.
'''