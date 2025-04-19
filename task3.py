import networkx as nx


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float("infinity") for vertex in graph.nodes()}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float("infinity"):
            break

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]["weight"]
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


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

all_shortest_paths = {}
for node in G.nodes():
    all_shortest_paths[node] = dijkstra(G, node)

print(all_shortest_paths)
