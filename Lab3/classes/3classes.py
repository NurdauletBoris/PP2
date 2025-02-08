class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)    
    def move(self, move_x, move_y):
        self.x = move_x
        self.y = move_y
    def dist(self, second_point):
        return ((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2) ** 0.5
        
p1 = Point(32,41)
p2 = Point(10,2)
p1.show()
p2.show()

print("Distance between two points:", int(p1.dist(p2)))