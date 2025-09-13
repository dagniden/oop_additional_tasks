"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
from datetime import datetime


class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = datetime.now() - self.start_time
        self.elapsed_time = end_time


with Timer() as timer:
    # блок кода
    total = 0
    for i in range(10_000_000):
        total += i
    # код для проверки 
print("Execution time:", timer.elapsed_time)
