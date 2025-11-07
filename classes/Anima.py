class Animal:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    def voice(self):
        print("Meaw")
class Cow(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    def voice(self):
        print("Maooo")

caty=Cat("caty",2,"white-brown")
jesi=Cow("jesi",4,"black")

def func(obj):
    obj.voice()
    
for i in [caty,jesi]:
    i.voice()

func(jesi)
print(callable(Cat))