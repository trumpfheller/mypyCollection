# Syntax [start:stop]
x = ["first", "second", "third", "fourth"]
print("get the first item only:")
print("by index")
print(x[0])
print("start at 0 and stops by 1")
print(x[0:1])
print("starts at -4 and goes back, stops at -3")
print(x[-4:-3])
print("get the Second item only:")
print(x[1])
print(x[1:2])
print(x[-2:-1])
print("get the third item only:")
print(x[2])
print(x[2:3])
print(x[-2:-1])

print("get the first and second item only:")
print(x[0:-2])
print("get the second and third item only:")
print(x[1:-1])

print("empty:")
print(x[1:1])
print(x[-1:0])
print(x[-1:1])
print(x[-1:-1])
print(x[-1:2])
