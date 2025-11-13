def power(n):
    return pow(n,3)
print(power(10))
class human:
    def __init__(self,name,family,age,color,gender):
        self.name=name
        self.family=family
        self.age=age
        self.color=color
        self.gender=gender
    
    def PersonDc(self):
        print(f"hello im {self.name} {self.family} and im {self.age} years old")
        
nima=human("nima","fakhimi","20","white","male")
nima.PersonDc()