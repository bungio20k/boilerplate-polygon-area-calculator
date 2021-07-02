class Rectangle:
    
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            picture = "Too big for picture."
        else:
            for i in range(self.height):
                for j in range(self.width):
                    picture += "*"
                picture += "\n"
        return picture
    
    def __str__(self):
        return "Rectangle(width=%d, height=%d)" % (self.width, self.height)

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)
    
class Square(Rectangle):

    def __init__(self, side = 0):
        Rectangle.__init__(self, side, side)
    
    def set_side(self, side = 0):
        self.set_height(side)
        self.set_width(side)

    def set_width(self, side = 0):
        self.height = side
        self.width = side

    def set_height(self, side = 0):
        self.height = side
        self.width = side
    
    def __str__(self):
        return "Square(side=%d)" % self.width