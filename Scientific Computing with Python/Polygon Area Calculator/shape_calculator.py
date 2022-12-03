class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        total_width = self.width * 2
        total_height = self.height * 2
        perimeter = total_width + total_height
        return perimeter

    def get_diagonal(self):
        w_sq = self.width ** 2
        h_sq = self.height ** 2
        diag = (w_sq + h_sq) ** .5
        return diag

    def get_picture(self):
        shape = ""
        if self.width > 50 or self.height > 50:
          shape += "Too big for picture."
        else:
          for i in range(self.height):
              shape += "*" * self.width + "\n"
        return shape

    def get_amount_inside(self, quad):
        if quad.width < self.width and quad.height < self.height:
            return int(self.get_area() / quad.get_area())
        else:
            return 0


class Square(Rectangle):
    def __init__(self, side):
        # super().__init__(self, side, side)
        Rectangle.__init__(self, width=side, height=side)
    
    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side
