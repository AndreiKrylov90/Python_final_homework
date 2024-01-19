# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# Добавляем логирование и ввод с командной строки

import logging
import sys

logging.basicConfig(filename='letter_counter.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def letter_counter(input_text):
    try:
        my_dict = {}
        for i in input_text:
            my_dict[i] = my_dict.get(i, 0) + 1

        return my_dict
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Enter some text without spaces, please try again")
        sys.exit(1)
    input_text = sys.argv[1]
    result = letter_counter(input_text)
    print(result)
