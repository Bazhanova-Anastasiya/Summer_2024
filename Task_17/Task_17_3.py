class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square

    def colour(self):
        self.colour = input()

    def square(self):
        self.colour = input()

    def info(self):
        print(f"{self.colour}: {self.square}")

a = Shape(input("Установите цвет объекта: "), int(input("Задайте площадь объекта, мм2: ")))
a.info()





