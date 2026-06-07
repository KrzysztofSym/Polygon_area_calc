class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
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
        picture = ""
        for _ in range(self.height):
            ("*" * self.width) + "\n"
        return picture
rect = Rectangle(10, 5)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_diagonal())