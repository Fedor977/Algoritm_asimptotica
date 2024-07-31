import sys
import time


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes  # Список узлов графа
        self.graph = self.construct_graph(nodes, init_graph)  # Конструкция графа на основе начальных данных

    def construct_graph(self, nodes, init_graph):
        '''
        Этот метод обеспечивает симметричность графика.
        Другими словами, если существует путь от узла A к B со значением V,
        должен быть путь от узла B к узлу A со значением V.
        '''
        graph = {}
        for node in nodes:  # Инициализация пустого словаря для каждого узла
            graph[node] = {}

        graph.update(init_graph)  # Обновляем граф с использованием данных из init_graph

        for node, edges in graph.items():  # Проходим по каждому узлу и его связям
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    # Если путь от соседнего узла к текущему отсутствует, добавляем его
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        "Возвращает узлы графа"
        return self.nodes  # Возвращаем список узлов

    def get_outgoing_edges(self, node):
        "Возвращает соседей узла"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                # Если существует ребро от node к out_node, добавляем out_node в список
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Возвращает значение ребра между двумя узлами."
        return self.graph[node1][node2]  # Возвращаем значение ребра между node1 и node2


def print_graph(graph):
    "Печатает граф в удобочитаемой форме"
    for node, edges in graph.items():
        for adjacent_node, value in edges.items():
            print(f"Edge from {node} to {adjacent_node} with value {value}")


def measure_time(graph, func, *args):
    "Измеряет время выполнения функции func"
    start_time = time.perf_counter()  # Используем более точный таймер
    result = func(*args)
    end_time = time.perf_counter()
    print(f"Execution time: {end_time - start_time:.9f} seconds")
    return result


if __name__ == '__main__':
    nodes = ["A", "B", "C", "D", "E", "F"]
    init_graph = {
        "A": {"B": 1, "C": 2},
        "B": {"A": 1, "D": 4, "E": 2},
        "C": {"A": 2, "F": 3},
        "D": {"B": 4},
        "E": {"B": 2, "F": 1},
        "F": {"C": 3, "E": 1}
    }

    graph_obj = Graph(nodes, init_graph)
    print("Constructed Graph:")
    print_graph(graph_obj.graph)

    print("\nOutgoing edges from node B:")
    measure_time(graph_obj.graph, graph_obj.get_outgoing_edges, "B")

    print("\nValue of edge between A and B:")
    measure_time(graph_obj.graph, graph_obj.value, "A", "B")
