S = int(input())

i = 0
sum_ = 0
while True:
    sum_ += i
    if sum_ > S:
        break
    
    i += 1
    
print(i-1)


print(sum(range(1,100000)))
