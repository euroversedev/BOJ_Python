s = input()

cnt = 0
i = 0
array = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
while True:
    if len(s) <= i: break
        
    cnt += 1
    
    for j in range(len(array)):
        if s[i:i+len(array[j])] == array[j]:
            i += len(array[j]) - 1
            break
    
    i += 1

print(cnt)



''' [review]
cnt2 = 0
for char in array:
    if char in s:
        cnt2 += s.count(char)
print(len(s) - cnt2)

in을 사용하면 문자열에서 해당 워드가 있는지 쉽게 알 수 있음.
문자열 s 기준이 아닌 크로아티아 알파벳 기준으로 깔끔하게 코딩 가능
'''