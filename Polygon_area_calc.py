class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return(f'Rectangle(width={self.width}, height={self.height})')
    def set_width(self, width):
        if width <= 0:
            raise ValueError("Width has to be positive")
        self.width = width   
    def set_height(self, height):
        if height <= 0:
            raise ValueError("Height has to be positive")
        self.height = height
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        return(2*(self.width + self.height))
    def get_diagonal(self):
        return((self.width **2 + self.height **2) **0.5)
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ""
        for _ in range(self.height):
            row = ("*" * self.width) + "\n"
            picture += row
        return picture
    def get_amount_inside(self, shape):
        fit_width = self.width // shape.width
        fit_height = self.height // shape.height
        return fit_width * fit_height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, side):
        if side <= 0:
            raise ValueError("Length has to be positive")
        self.width = side
        self.height = side
    def set_height(self, side):
        self.set_width(side)
    def set_side(self, side):
        self.set_width(side)    
    def __str__(self):
        return(f'Square(side={self.width})')  
        
rect = Rectangle(10, 5)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_diagonal())
print(rect.get_picture())
print(rect)

sq = Square(9)
print(sq.get_picture())
print(sq)