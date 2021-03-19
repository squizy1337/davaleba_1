class Rectangle:
    def __init__(self, width, lenght):
        self.width = width
        self.lenght = lenght

    def area(self):
        return self.width * self.lenght

    def perimeter(self):
        return (self.width + self.lenght)* 2
    def print_info(self):
        return f"სიგრძე - {self.width}, სიგანე - {self.lenght}, ფართობი - {self.area()}, პერიმეტრი - {self.perimeter()}"

if __name__ == '__main__':
    cout= Rectangle(2,5)
    print(cout.print_info())