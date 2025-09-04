#change value in tuple
x = ("audi" , "bmw", "mercedes")
y = list(x)
y[0] = "ferrari"
x = tuple(y)
print(x)

#add value in tuple
x = ("audi" , "bmw", "mercedes")
y = list(x)
y.append("ferrari")
x = tuple(y)
print(x)