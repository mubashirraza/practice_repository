class Teddy:#class
     quantity = 200# calss attribute
     def __init__(self,name,color): 
         self.name = name
         self.color = color

'''teddy1 = Teddy("ted","red")#object\
print(teddy1.name)
print(teddy1.color)

teddy2 = Teddy("rob","brown")
print(teddy2.name)
print(teddy2.color)'''

def change_color(self,color):
        print("thid is method")
        self.color = color

teddy1 = Teddy("ted","red")#object\
print(teddy1.name)
print(teddy1.color)

teddy1.change_color("orange")
print(teddy1.name)
print(teddy1.color)
    
     
    
