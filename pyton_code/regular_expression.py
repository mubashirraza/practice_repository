import re#regular expression



pattern = r"eggs"

if re.match(pattern,"baconeggseggseggs"):
    print("match found")
else:
    print("no match found")

if re.search(pattern,"baconeggseggseggs"):
      print("match found")
else:
    print("no match found")
    #o/p no match found
           # match found

if re.findall(pattern,"baconeglgseglgseggs"):
      print("match found")
else:
    print("no match found")

print(re.findall(pattern,"baconeggseggseglgs"))

#find and replace
import re
string = "my name is john, hii i am john"
pattern = r"john"
newstring = re.sub(pattern,"rub",string)
print(newstring)

#o/p my name is rub, hii i am rub
#sub function present in re module
#sub function is replace the word
