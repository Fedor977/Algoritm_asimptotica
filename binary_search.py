"""
В целом метод бинарного поиска можно описать следующим образом.
Сначала в возрастающем или убывающем множестве определяется среднее значение,
после чего оно сравнивается с искомым.
При совпадении заданного и центрального элемента поиск прекращается — элемент считается найденным.
"""
def binary_search(arr, x):
    """Бинарный поиск"""
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid  # Возвращаем индекс, если элемент найден
        elif arr[mid] < x:
            l = mid + 1  # Ищем в правой половине
        else:
            r = mid - 1  # Ищем в левой половине
    return -1  # Элемент не найден

arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
print(f"Element found at index {result}" if result != -1 else "Element not found")
