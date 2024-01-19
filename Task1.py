# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Добавляем логирование и ввод с командной строки

import logging
import sys

logging.basicConfig(filename='sorter.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def sorter(numbers):
    try:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print("I need a list of numbers")
            sys.exit(1)
        input_numbers = [int(arg) for arg in sys.argv[1:]]
        result = sorter(input_numbers)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        logging.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
