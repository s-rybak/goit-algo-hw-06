from collections import deque
import networkx as nx


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print("->", end=" ")  # Відвідуємо вершину
    print(vertex, end=" ")  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print("->", end=" ")
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)


G = nx.DiGraph(name="Small city network")

objects = {
    "Train station": (0, 0),
    "Center": (2, 2),
    "Independence square": (4, 2),
    "University": (6, 2),
    "Market": (3, 5),
    "Hospital": (3, 0),
    "Park": (6, 0),
    "Stadium": (8, 4),
    "Residential area1": (1, 1),
    "Residential area2": (1, 1),
}


paths = [
    ("Train station", "Center", 7),
    ("Center", "Independence square", 7),
    ("Independence square", "Market", 11),
    ("Market", "Park", 6),
    ("Park", "University", 6),
    ("University", "Hospital", 6),
    ("Stadium", "Park", 8),
    ("Stadium", "Hospital", 8),
    ("Park", "Residential area1", 8),
    ("Residential area1", "Center", 8),
    ("Center", "Park", 8),
    ("Park", "Hospital", 8),
    ("Stadium", "Residential area2", 8),
    ("Residential area2", "University", 8),
    ("Residential area2", "Hospital", 8),
]


def add_nodes(G, objects):
    for object in objects:
        G.add_node(object, pos=objects[object])


def add_path(G, paths):
    for path in paths:
        G.add_edge(path[0], path[1], weight=path[2])
        G.add_edge(path[1], path[0], weight=path[2])


add_nodes(G, objects)
add_path(G, paths)

print("DFS path:")
dfs_recursive(G, "Train station")
print("\n")
print("BFS path:")
bfs_recursive(G, deque(["Train station"]))
