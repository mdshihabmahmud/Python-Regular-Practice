thistuple = ("apple", "banana", "cherry")
print(thistuple)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "mango"
x = tuple(y)

print(x)
