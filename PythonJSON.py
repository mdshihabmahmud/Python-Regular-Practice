import json

# some JSON:
x = '{ "name":"Shihab", "age":21, "city":"Dhaka"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
