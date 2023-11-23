# импортируем модуль для работы с логами
import logging

# создаем логгер
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# создаем обработчик для записи в файл
handler = logging.FileHandler('game.log')
handler.setLevel(logging.INFO)

# создаем форматтер для логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# добавляем обработчик к логгеру
logger.addHandler(handler)

# функция для получения ввода пользователя с проверкой на корректность
def get_input(prompt, input_type):
    while True:
        try:
            user_input = input(prompt)
            if input_type == int:
                user_input = int(user_input)
            elif input_type == str:
                user_input = str(user_input)
            else:
                raise ValueError
            return user_input
        except ValueError:
            print("Некорректный ввод. Попробуйте еще раз.")

# функция для генерации случайного числа от 1 до N
def generate_number(N):
    import random
    number = random.randint(1, N)
    logger.info(f'Загадано число: {number}')
    return number

# функция для игры
def play_game():
    # получаем от пользователя число N и количество попыток k
    N = get_input("Введите число N: ", int)
    k = get_input("Введите количество попыток k: ", int)

    # генерируем случайное число от 1 до N
    number = generate_number(N)

    # цикл для k попыток пользователя
    for i in range(k):
        # получаем от пользователя число guess
        guess = get_input("Введите число: ", int)

        # проверяем, угадал ли пользователь число
        if guess == number:
            print("Вы угадали!")
            logger.info(f'Пользователь угадал число {number}')
            return
        elif guess < number:
            print("Загаданное число больше.")
            logger.info(f'Пользователь ввел число {guess}. Загаданное число больше.')
        else:
            print("Загаданное число меньше.")
            logger.info(f'Пользователь ввел число {guess}. Загаданное число меньше.')

    # если пользователь не угадал число за k попыток
    print("Попытки закончились.")
    logger.info('Попытки пользователя закончились')

# запускаем игру
play_game()
