"""name = ["muabshir","mayur",'ayesha',"kajal"]
print(name[3])
numbers = [1,2,3,4,5,6,8]
print(numbers)
newnumbers = [1,1,2,2,2,2,3,]
#print(numbers+newnumbers)
#print(numbers*50)
abc = []
print(abc)


name = ["muabshir","mayur",'ayesha',"kajal"]
#print ("mayur" in name)
#print ("wido" in name)         function in list
#name.append("bushra") -1
#print(name)

#print (len(name)) -2

#name.insert(1,"raza")-3
#print(name)

print (name.index("mayur"))  #-4"""

# list slicing
numbers =[0,100,200,300,400,500,600,700,800]
print(numbers[2:5])# o/p 200,300,400,500
print(numbers[:3])# o/p 0,100,200
print(numbers[3:])# o/p 0,300,400,500,600,700,800
print(numbers[1:9:2])# o/p 100,300,500,700

# list comprehension
list = [x**2 for x in range(5)]
print(list) #o/p 0, 1, 4, 9, 16 sqaure of the no.

list = [x**2 for x in range(10) if x**2 %2 ==0 ]
print(list)


