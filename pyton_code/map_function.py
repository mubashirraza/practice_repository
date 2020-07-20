def add(x):
    return x+2
newlist = [10, 20, 30, 40, 50]

result = list(map(add,newlist))

print(result)
# o/p 12, 22, 32, 42, 52  add the function to list


'''def add(x):
    return x+2'''
newlist = [10, 20, 30, 40, 50]

result = list(map(lambda x: x+2,newlist))

print(result)
