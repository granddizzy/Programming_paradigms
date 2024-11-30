from math import sqrt
from functools import reduce
from typing import List

# Функция для вычисления среднего значения массива
def mean(values: List[float]) -> float:
    # Суммируем элементы и делим на количество
    return reduce(lambda acc, v: acc + v, values) / len(values)

# Функция для вычисления коэффициента корреляции Пирсона
def pearson_correlation(x: List[float], y: List[float]) -> float:
    # Проверяем, что длины массивов одинаковы
    if len(x) != len(y):
        raise ValueError("Длины массивов должны совпадать")

    # Вычисляем средние значения для массивов x и y
    x_mean = mean(x)
    y_mean = mean(y)

    # Создаем список отклонений (каждое значение минус среднее)
    deviations = list(zip(
        map(lambda xi: xi - x_mean, x),
        map(lambda yi: yi - y_mean, y)
    ))

    # Вычисляем числитель формулы: сумма произведений отклонений
    numerator = reduce(lambda acc, pair: acc + pair[0] * pair[1], deviations, 0)

    # Вычисляем знаменатель: произведение корней сумм квадратов отклонений
    denominator_x = sqrt(reduce(lambda acc, xi: acc + xi ** 2, (xi for xi, _ in deviations), 0))
    denominator_y = sqrt(reduce(lambda acc, yi: acc + yi ** 2, (yi for _, yi in deviations), 0))

    # Возвращаем итоговый коэффициент корреляции
    return numerator / (denominator_x * denominator_y)


x = [10, 20, 30, 40, 50]
y = [15, 25, 35, 45, 55]

correlation = pearson_correlation(x, y)
print(f"Коэффициент корреляции Пирсона: {correlation}")
