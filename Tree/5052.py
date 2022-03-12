import sys

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    
    
    phonebook = set()
    for _ in range(N):
        phonenumber = sys.stdin.readline().strip()
        phonenumber = phonenumber.replace(" ", "")

        phonebook.add(phonenumber)
    
    flag = True
    for phonenumber in phonebook:
        for i in range(1, len(phonenumber)):
            if phonenumber[:i] in phonebook:
                flag = False
        
    
    if flag: print("YES")
    else: print("NO")
        
'''
위 코드는 set을 이용한 해시로 구현했지만,

"파이썬의 문자열 sort 특성" 또는 "Trie알고리즘"을 통해 구현이 가능하다.
Trie알고리즘은 검색엔진에 주로 이용되며 시간복잡도가 문자열의 길이값과 같다.(매우빠름)
'''