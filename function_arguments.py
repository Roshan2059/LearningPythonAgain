def add(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print(sum)
add(1,2,3,4,5,6,7,8,9,10)

def subtract(a,b):
    return a - b

# c = subtract(10,5)
print("The result is: ", subtract(10,5))