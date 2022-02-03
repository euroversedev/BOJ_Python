N = int(input())
array = list(map(int, input().split())) 

start = 0
end = 0
i = 0
total = 0

i = 1
while True:
    if N <= i : break
    total += array[i]
    
    if sum(array[start:end+1]) < total:
        end = i
    
    if total < 0:
        total = 0
        start, end = i+1, i+1
        

    i += 1
        

while True:
    if N <= i: break
        
    if result + array[i] <= 0:
        result = 0
        start, end = i + 1, i + 1
    
    if sum(array[start:end+1]) < result + array[i]:
        end = i
    
    result += array[i]
    i += 1
    print(result, end =" ")

print(start, end)
print(sum(array[start:end+1]))