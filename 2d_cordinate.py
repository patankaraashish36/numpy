class Point:
    def __init__(self, x, y) -> None:
        self.x_cod = x
        self.y_cod = y
    
    def __str__(self) -> str:
        return f"<{self.x_cod},{self.y_cod}>"
    
    def eucladian_distance(self, other):
        print(((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5)
    
    def distance_f_origin(self):
        # return self.eucladian_distance(Point(0,0))
        print(((self.x_cod - 0)**2 + (self.y_cod - 0)**2)**0.5)
    
class Line:
    def __init__(self, A, B, C) -> None:
        self.A = A
        self.B = B
        self.C = C
        
    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C}"
    
    # def lies_on_line(line, point):
    def lies_on_line(self, point):
        print(f"<{point.x_cod},{point.y_cod}>")
        if (point.x_cod * self.A  + point.y_cod * self.B + self.C) == 0:
            print("Yes lies.")
        else:
            print("No lies.")
    
    # def shorttest_distance(line, point):
    def shorttest_distance(self, point):
        print(abs(self.A*point.x_cod + self.B*point.y_cod + self.C)/(self.A**2 + self.B**2)**0.5)
    
p1 = Point(3,4)
p2 = Point(1,1)
# p1.distance_f_origin()

l1 = Line(1,1,-2)
print(l1)

l1.lies_on_line(p1)
l1.shorttest_distance(p2)