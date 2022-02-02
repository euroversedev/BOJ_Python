N = int(input())
cnt = 0

for _ in range(N):
    flag = True
    spelling = set()
    
    word = input()
    post = word[0]
    for i in range(len(word)):
        if (word[i] in spelling) and (word[i] != post):
            flag = False
        post = word[i]
        spelling.add(word[i])
    
    if flag == True: cnt += 1

print(cnt)

''' [review]
1. set 조합 자료형의
데이터 삽입 : set.add(하나) or set.update(여러개)
데이터 삭제 : set.remove(원소)

2. 문자열 앞쪽의 철자를 확인할 때,
굳이 조합 자료형에 넣을 필요없이! 슬라이싱을 이용하면 편함.
ex. if word[i] in word[:i]
'''