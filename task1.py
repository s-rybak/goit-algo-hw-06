import networkx as nx
import matplotlib.pyplot as plt

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


def analyze_network(G):
    print("The name of the network: ", G.name)
    print("The number of vertices: ", G.number_of_nodes())
    print("The number of edges: ", G.number_of_edges())
    print("The degree of vertices: ", nx.degree(G))


def visualize_network(G):
    nx.draw(G, with_labels=True)
    plt.show()


add_nodes(G, objects)
add_path(G, paths)
analyze_network(G)
visualize_network(G)
