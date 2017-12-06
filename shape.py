class Shape:
    def __init__(self, id_sh, x, y):
        self.Id_Sh, self.X, self.Y = id_sh, x, y
    
    def id_sh(self):
        return self.Id_Sh
    
    def x(self, *new_x):
        if new_x:
            self.X = new_x
        else:
            return self.X
    
    def y(self, *new_y):
        if new_y:
            self.Y = new_y
        else:
            return self.Y
    
    def info(self):
        return '(%d, %d)' % (self.X, self.Y)
    

class Circle(Shape):
    def __init__(self, id_sh, x, y, r):
        self.Id_Sh, self.X, self.Y, self.R = id_sh, x, y, r
    
    def r(self, *new_r):
        if new_r:
            self.R = new_r
        else:
            return self.R 
    def info(self):
            return '(%d, %d, %d)' % (self.X, self.Y, self.R)    
a = Shape(123, 1, 1)
print(a.info())
print(a.x())

a = Circle(123, 1, 1, 20)
print(a.info())
print(a.x())
print(a.r())