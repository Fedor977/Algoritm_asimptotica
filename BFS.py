"""
Алгоритм поиска в ширину (англ. breadth-first search, BFS)
позволяет найти кратчайшие пути из одной вершины невзвешенного
(ориентированного или неориентированного) графа до всех остальных вершин.
Под кратчайшим путем подразумевается путь, содержащий наименьшее число ребер.
"""

import collections
import time

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])  # Создаём множество для посещённых вершин и очередь для обхода
    visited.add(root)  # Добавляем корневую вершину в посещённые

    while queue:  # Пока есть элементы в очереди
        vertex = queue.popleft()  # Извлекаем вершину из начала очереди
        print(f"Visited {vertex}")  # Выводим посещённую вершину

        for neighbour in graph[vertex]:  # Проходим по всем соседям вершины
            if neighbour not in visited:  # Если сосед не посещён
                visited.add(neighbour)  # Добавляем его в посещённые
                queue.append(neighbour)  # Добавляем соседа в очередь

def measure_bfs_time(graph, root):
    start_time = time.time()  # Фиксируем время начала
    bfs(graph, root)  # Запускаем BFS
    end_time = time.time()  # Фиксируем время окончания
    return end_time - start_time  # Возвращаем время выполнения

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}  # Определяем граф в виде словаря смежности
    execution_time = measure_bfs_time(graph, 0)  # Измеряем время выполнения BFS с вершины 0
    print(f"BFS execution time: {execution_time:.9f} seconds")  # Выводим время выполнения BFS



