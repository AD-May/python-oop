class Rectangle:
    width: float | int
    height: float | int

    def __init__(self, width, height):
        if width <= 0:
            raise ValueError("Width must be greater than 0")
        elif height <= 0:
            raise ValueError("Height must be greater than 0")
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        if width <= 0:
            raise ValueError("New width must be greater than 0")
        self.width = width

    def set_height(self, height):
        if height <= 0:
            raise ValueError("New height must be greater than 0")
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
            return "Too big for picture."
        for _ in range(self.height):
            picture += f"{'*' * self.width}\n"
        return picture

    def get_amount_inside(self, shape):
        available_area = self.width * self.height
        inserted_shape_area = shape.get_area()

        return available_area // inserted_shape_area


class Square(Rectangle):
    
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, side_length):
        super().set_width(side_length)
        super().set_height(side_length)

    def set_height(self, side_length):
        super().set_width(side_length)
        super().set_height(side_length)

    def set_side(self, side_length):
        if side_length <= 0:
            raise ValueError("New side length must be greater than 0")
        self.set_width(side_length)
        
    

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))