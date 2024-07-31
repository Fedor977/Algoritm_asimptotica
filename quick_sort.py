"""
Из массива выбирается опорный элемент, с ним сравниваются остальные элементы и
помещаются справа или слева, в зависимости от значения функция повторяется.
"""

def quick_sort(arr):
    """Быстрая сортировка"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного
    return quick_sort(left) + middle + quick_sort(right)

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)  # [1, 1, 2, 3, 6, 8, 10]
