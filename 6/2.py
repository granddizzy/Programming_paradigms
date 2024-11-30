# Функциональная парадигма
# Используем рекурсию и избегаем изменения состояния переменных

def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]
target = 4
result = binary_search(arr, target)

if result != -1:
    print(f"Элемент найден на индексе: {result}")
else:
    print("Элемент не найден в массиве.")
