'''
Реализация набора фигур с использованием ООП

Цель: Разработать систему классов для работы с геометрическими фигурами, используя
основные принципы объектно-ориентированного программирования: наследование,
абстракция, инкапсуляция и полиморфизм
'''

from abc import ABC, abstractmethod
import math

class Figure(ABC):
    """
    Абстрактный класс для представления геометрической фигуры.
    """

    @abstractmethod    #принцип абстракции  
    def area(self) -> float:
        """
        Метод для расчета площади фигуры.
        """
        pass

    @abstractmethod    #принцип абстракции  
    def perimeter(self) -> float:
        """
        Метод для расчета периметра фигуры.
        """
        pass

class Square(Figure):
    """
    Класс для представления квадрата.
    """

    def __init__(self, side: float):
        self._side = side

    def area(self) -> float:
        return self._side ** 2

    def perimeter(self) -> float:
        return 4 * self._side

class Rectangle(Figure):
    """
    Класс для представления прямоугольника.
    """

    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)

class Triangle(Figure):
    """
    Класс для представления треугольника.
    """

    def __init__(self, a: float, b: float, c: float):
        self._a = a
        self._b = b
        self._c = c

    def area(self) -> float:
        semi_perimeter = self.perimeter() / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self._a) * (semi_perimeter - self._b) * (semi_perimeter - self._c))

    def perimeter(self) -> float:
        return self._a + self._b + self._c

class Circle(Figure):
    """
    Класс для представления окружности.
    """

    def __init__(self, radius: float):
        self._radius = radius

    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

class Rhombus(Figure):
    """
    Класс для представления ромба.
    """

    def __init__(self, side: float, height: float):
        self._side = side
        self._height = height

    def area(self) -> float:
        return self._side * self._height

    def perimeter(self) -> float:
        return 4 * self._side
    
class Trapezoid(Figure):
    """
    Класс для представления трапеции.
    """

    def __init__(self, a: float, b: float, height: float):
        self._a = a
        self._b = b
        self._height = height

    def area(self) -> float:
        return ((self._a + self._b) / 2) * self._height

    def perimeter(self) -> float:
        # Для упрощения, считаем, что боковые стороны равны и равны 1
        side_length = math.sqrt(((self._b - self._a) / 2) ** 2 + self._height ** 2)
        return self._a + self._b + 2 * side_length

# Пример использования
def main():
    figures = [
        Square(4),
        Rectangle(3, 5),
        Triangle(3, 4, 5),
        Circle(2),
        Rhombus(3, 4)
    ]

    for figure in figures:
        print(f"{figure.__class__.__name__}: Area = {figure.area():.2f}, Perimeter = {figure.perimeter():.2f}")

if __name__ == "__main__":
    main()

