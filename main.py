import random  # Импортируем модуль для генерации случайных чисел
import time    # Импортируем модуль для измерения времени выполнения


def bubble_sort(arr):
    """Пузырьковая сортировка"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Обмен элементов
    return arr


def quick_sort(arr):
    """Быстрая сортировка"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Опорный элемент
    left = [x for x in arr if x < pivot]    # Элементы меньше опорного
    middle = [x for x in arr if x == pivot] # Элементы, равные опорному
    right = [x for x in arr if x > pivot]   # Элементы больше опорного
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """Сортировка слиянием"""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]  # Левая половина
        R = arr[mid:]  # Правая половина

        merge_sort(L)  # Рекурсивная сортировка левой половины
        merge_sort(R)  # Рекурсивная сортировка правой половины

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):  # Копирование оставшихся элементов L
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):  # Копирование оставшихся элементов R
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def selection_sort(arr):
    """Сортировка выбором"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Находим индекс минимального элемента
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Обмен элементов
    return arr


def binary_search(arr, x):
    """Бинарный поиск"""
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid  # Элемент найден, возвращаем индекс
        elif arr[mid] < x:
            l = mid + 1  # Продолжаем искать в правой половине
        else:
            r = mid - 1  # Продолжаем искать в левой половине
    return -1  # Элемент не найден


def measure_time(sort_func, arr):
    """Измерение времени выполнения функции сортировки"""
    start_time = time.time()  # Запуск таймера
    sorted_arr = sort_func(arr.copy())  # Копируем массив и сортируем
    end_time = time.time()  # Остановка таймера
    return end_time - start_time  # Возвращаем время выполнения


if __name__ == "__main__":
    # Генерация случайных данных
    array_size = 1000
    random_array = [random.randint(1, 1000) for _ in range(array_size)]

    # Измерение времени выполнения алгоритмов сортировки
    bubble_time = measure_time(bubble_sort, random_array)
    quick_time = measure_time(quick_sort, random_array)
    merge_time = measure_time(merge_sort, random_array)
    selection_time = measure_time(selection_sort, random_array)

    # Вывод времени выполнения каждого алгоритма
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
    print(f"Quick Sort Time: {quick_time:.6f} seconds")
    print(f"Merge Sort Time: {merge_time:.6f} seconds")
    print(f"Selection Sort Time: {selection_time:.6f} seconds")

    # Пример бинарного поиска
    sorted_array = sorted(random_array)  # Сортируем массив для бинарного поиска
    search_element = random.choice(random_array)  # Выбираем случайный элемент для поиска
    search_time = measure_time(lambda arr: binary_search(arr, search_element), sorted_array)
    print(f"Binary Search for {search_element} took {search_time:.6f} seconds")
