"""
В информатике алгоритм Флойда–Уоршелла - это алгоритм поиска кратчайших путей
во взвешенном графе с положительным или отрицательным весом ребер.
За одно выполнение алгоритма будут найдены длины кратчайших путей между всеми парами вершин.
"""

import math
import time  # Импортируем модуль для замера времени

def get_path(P, u, v):
    path = [u]  # Начинаем путь с вершины u
    while u != v:  # Пока не достигнем вершины v
        u = P[u][v]  # Переходим к предыдущей вершине на пути от u к v
        path.append(u)  # Добавляем вершину в путь

    return path[::-1]  # Возвращаем путь в правильном порядке (от начальной до конечной)

V = [[0, 2, math.inf, 3, 1, math.inf, math.inf, 10],
     [2, 0, 4, math.inf, math.inf, math.inf, math.inf, math.inf],
     [math.inf, 4, 0, math.inf, math.inf, math.inf, math.inf, 3],
     [3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8],
     [1, math.inf, math.inf, math.inf, 0, 2, math.inf, math.inf],
     [math.inf, math.inf, math.inf, math.inf, 2, 0, 3, math.inf],
     [math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 1],
     [10, math.inf, 3, 8, math.inf, math.inf, 1, 0],
]

N = len(V)  # Число вершин в графе
P = [[v for v in range(N)] for u in range(N)]  # Инициализируем матрицу предыдущих вершин для поиска кратчайших маршрутов

start_time = time.time()  # Засекаем время начала выполнения алгоритма

# Алгоритм Флойда-Уоршелла для нахождения кратчайших путей
for k in range(N):
    for i in range(N):
        for j in range(N):
            d = V[i][k] + V[k][j]  # Вычисляем вес пути через вершину k
            if V[i][j] > d:  # Если путь через k короче текущего пути от i к j
                V[i][j] = d  # Обновляем вес пути
                P[i][j] = k  # Обновляем промежуточную вершину

end_time = time.time()  # Засекаем время окончания выполнения алгоритма
execution_time = end_time - start_time  # Вычисляем время выполнения алгоритма

# Нумерация вершин начинается с нуля
start = 1  # Начальная вершина
end = 4  # Конечная вершина

# Печатаем путь от вершины start до вершины end
print("Путь от вершины", start, "до вершины", end, ":", get_path(P, end, start))

# Печатаем время выполнения алгоритма
print(f"Время выполнения алгоритма: {execution_time:.6f} секунд")
