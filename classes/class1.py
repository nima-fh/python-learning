import math
""""Point class is class that show us point in 2d board and this poin can move in board"""
# The class `Point` defines methods for resetting, moving, and calculating distance between points in
# a 2D space.
class Point: 
    x=20
    y=10
    __z="private value"
    def Reset(self):
        self.x=0
        self.y=0
         
    def move(self,x,y):
        self.x=self.x+x
        self.y=self.y+y
        
    def distance(self,p2:"Point"):
        return math.hypot(self.x-p2.x,self.y-p2.y)
    
    print(__z)
        
        
        
p1=Point()
p1.x=2
p1.y=3
p2=Point()
p2.x=1
p2.y=1
print("x:",p1.x,"y:",p1.y)
p1=Point()
p1.x=2
p1.y=3
print("x:",p1.x,"y:",p1.y)
p1.move(-4,5)
print("x:",p1.x,"y:",p1.y)
distance=p1.distance(p2)
print(distance)
p1.Reset()
print("x:",p1.x,"y:",p1.y)
p3=Point()
print(p3.x)
print(p3.y)
print(p1.__z)


