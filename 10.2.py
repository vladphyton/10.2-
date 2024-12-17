import threading
from time import perf_counter, sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        days = 0
        start_time = perf_counter()  # Засекаем время начала сражения

        while enemy > 0:
            days += 1
            enemy -= self.power
            sleep(1)
            print(f'{self.name} сражается {days} день(дня)..., осталось {enemy if enemy > 0 else 0} воинов.')

        end_time = perf_counter()  # Засекаем время окончания сражения
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


# Создание и запуск потоков
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
