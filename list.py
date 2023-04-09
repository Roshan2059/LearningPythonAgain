name = ["roshan", 100, "sudip", 90, "jiban", 80]
if "sudip" in name:
    print("yes")
else:
    print("NO")
print(name[-3])

print(name[2:5])
print(name[2:len(name):2])

list1 = [i+1 for i in range(10)]
print(list1)

list2 = [i for i in range(100) if i%2 == 0]
print(list2)
