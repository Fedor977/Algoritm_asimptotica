"""
Двои́чное де́рево — иерархическая структура данных, в которой
каждый узел имеет не более двух потомков.
Как правило, первый называется родительским узлом,
а дети называются левым и правым наследниками.
"""

import time  # Импортируем модуль для замера времени


class TreeNode:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.left = None  # Левый дочерний узел
        self.right = None  # Правый дочерний узел


def insert(root, value):
    """ Вставляет новый узел со значением value в бинарное дерево """
    if root is None:  # Если дерево пустое
        return TreeNode(value)  # Создаем новый узел
    else:
        if value < root.value:  # Если значение меньше, чем текущее значение
            root.left = insert(root.left, value)  # Рекурсивно вставляем в левое поддерево
        else:
            root.right = insert(root.right, value)  # Рекурсивно вставляем в правое поддерево
    return root  # Возвращаем корень дерева


def inorder_traversal(root):
    """ Выполняет обход бинарного дерева в порядке 'левый узел - корень - правый узел' """
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(
        root.right) if root else []  # Рекурсивный обход


# Временные замеры
start_time = time.time()  # Записываем время начала выполнения

# Создание бинарного дерева
root = None  # Инициализируем пустое дерево
values = [7, 3, 10, 1, 5, 8, 12]  # Значения для вставки в дерево
for value in values:
    root = insert(root, value)  # Вставляем значения в дерево

# Обход бинарного дерева
traversal_result = inorder_traversal(root)  # Получаем результат обхода

end_time = time.time()  # Записываем время окончания выполнения
execution_time = end_time - start_time  # Вычисляем время выполнения

print("Результат обхода дерева в порядке 'левый узел - корень - правый узел':",
      traversal_result)  # Печатаем результат обхода
print(f"Время выполнения: {execution_time:.6f} секунд")  # Печатаем время выполнения
