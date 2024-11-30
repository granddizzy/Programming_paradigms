# Объектно-ориентированная парадигма

class BinarySearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, target):
        left, right = 0, len(self.arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


arr = [1, 3, 4, 6, 7, 8, 10, 13, 14]
searcher = BinarySearch(arr)
result = searcher.search(4)
print(f"Элемент найден на индексе: {result}" if result != -1 else "Элемент не найден.")
