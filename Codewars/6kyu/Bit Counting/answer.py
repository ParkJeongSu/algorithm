def count_bits(n):
    str = bin(n)
    answer = 0
    for i in str:
        if i =='1':
            answer +=1
    return answer

v = [0,4,7,9,10]

for i in v:
    print(count_bits(i))