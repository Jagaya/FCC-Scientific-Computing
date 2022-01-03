class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __repr__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) +")"
        
    def set_width(self, new):
        self.width = new
        
    def set_height(self, new):
        self.height = new
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2*self.width + 2*self.height)
    
    def get_diagonal(self):
        return ( self.width**2 + self.height**2 )**0.5
    
    def get_picture(self):
        output = ""
        if self.width > 50 or self.height > 50:
            output = "Too big for picture."
        else:
            for i in range(self.height):
                output += "*" * self.width + "\n"
                
        return output
    
    def get_amount_inside(self, shape):
        amount = 1
        amount *= self.height // shape.height
        amount *= self.width // shape.width
        return amount
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def __repr__(self):
        return "Square(side=" + str(self.height) + ")"
        
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
        print(self.width, self.height)
        
    def set_height(self, side):
        self.set_side(side)
        
    def set_width(self, side):
        self.set_side(side)