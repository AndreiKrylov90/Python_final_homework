# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.
# Добавляем логирование и ввод с командной строки

import logging
import sys

logging.basicConfig(filename='rectangle.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        if b:
            self.b = b
        else:
            self.b = a

    def perimeter(self):
        return 2 * self.a + 2 * self.b

    def area(self):
        return self.a * self.b

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print("I need width and height for our rectangle")
            sys.exit(1)
        side_length1 = int(sys.argv[1])
        side_length2 = int(sys.argv[2]) if len(sys.argv) == 3 else None
        rect_1 = Rectangle(side_length1, side_length2)
        print(f"Perimeter: {rect_1.perimeter()}, Area: {rect_1.area()}")
    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
