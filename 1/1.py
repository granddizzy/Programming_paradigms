
def sort_list_imperative(numbers):
    """
    Императивный стиль. Сортировка пузырьком.
    :param numbers:
    :return:
    """
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sort_list_imperative(numbers)
print("Отсортированный список:", sorted_numbers)
