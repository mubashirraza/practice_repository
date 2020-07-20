'''numbers = [4,5,6]
newstring = "numbers:{0}/{1}/{2}".format(numbers[0],numbers[1],numbers[2])
print(newstring)



a= "{x}/{y}/{z}".format(x=100,y=200,z=99)
print(a)'''

print(":".join(["mayur","jannat","sakshi"]))# how to seprated using string function
#o/p mayur:jannat:sakshi------1

newstring = "hello there"
print(newstring.replace("there","world"))#o/p hello world// replce the word
                                        #---2
newstring = "this is a string"
print(newstring.startswith("this")) #o/p True ----3


newstring = "this is a string"
print(newstring.endswith("this"))#o/p false

newstring = "this is a string"
print(newstring.endswith("string"))#o/p True ----4


newstring = "this is a string"
print(newstring.upper())#o/p  THIS IS A STRING  ---5

ewstring = "THIS IS A STRING"
print(newstring.lower())#o/p this is a string

            #Numeric function
print(max( 1,2,3,4,5,6,7,98))# max value
print(min( 1,2,3,4,5,6,7,98))#min value
print(abs(-208)) #always +ve

#que
newlist = list(range(1, 100))

for x in newlist:

    if x % 2 != 0:
        print (x)

