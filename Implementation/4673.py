array = [0] * 10036   # 각 인덱스에 해당하는 번호의 생성자를 저장하는 리스트
                                      # Ex. array[101] = 91, 100
    
for i in range(1, 10001):
    result = i + sum(map(int, str(i)))
    array[result] = i

for i in range(1, 10001):
    if array[i] == 0: print(i)
    
