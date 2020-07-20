import re

pattern = r"mu.r"  #only . replace the other character in 

if re.match(pattern,"mubr"):
    print("match found")

pattern = r"^gr.y$"    #^ carret sign

if re.match(pattern,"grby"):
    print("match found")

#character  class
#MH31C2010
pattern = r"[A-Z][A-Z][0-9][0-9][A-Z][0-9][0-9][0-9][0-9]"
if re.search(pattern,"MH31C2010"):
    print("match founddd")
# starmetacharacter
pattern = r"eggs(bacon)*"
if re.match(pattern,"eggsbacon"):
    print("match founded")

#group
pattern = r"bread(eggs)*bread"
if re.match(pattern,"breadeggseggsbread"):
    print("match found")
    


