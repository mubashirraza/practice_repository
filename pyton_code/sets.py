numbers = {1,2,3,4,5,6}
numbers.add(9)
numbers.remove(3)
print(numbers)
#union operation in two sets- no duplicate value
seta = {1,2,3,4,5,6}
setb = {7,8,9,5,6,7}
print(seta | setb)
#intersection common between in two sets
seta = {1,2,3,4,5,6}
setb = {7,8,9,5,6,7}
print(seta & setb)

#diff operation- present in set a but not in b
seta = {1,2,3,4,5,6}
setb = {1,2,7,8,9,5,6,7}
print(seta - setb)

