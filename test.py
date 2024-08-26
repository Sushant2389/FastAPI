dic1 = [25]
dic2 = dic1

print("before:")
print(dic1)
print(dic2)
print("id dic1",id(dic1))
print("id dic2",id(dic2))

dic2[0] = 55

print("After:")
print(dic1)
print(dic2)
print("id dic1",id(dic1))
print("id dic2",id(dic2))


dic3 = [100]
dic2 =dic3
print("Finally:")
print(dic1)
print(dic2)
print(dic3)

print("id dic1",id(dic1))
print("id dic2",id(dic2))
print("id dic3",id(dic3))

