#itertools inn functional programming


from itertools import count

for i in count(3):
    print(i)

    if i >= 20:
        break
"""o/p 3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20"""
#accumulate function
from itertools import accumulate,takewhile
numbers = list(accumulate(range(8)))
print(numbers)
print(list(takewhile(lambda x:x <=10,numbers)))
#o/p [0, 1, 3, 6, 10, 15, 21, 28]
# o/p[0, 1, 3, 6, 10] less than 10 using takewhile
