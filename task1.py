import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph(name="Small city network")

objects = {
    "Train station": (0, 0),
    "Center": (2, 2),
    "Independence square": (4, 2),
    "University": (6, 2),
    "Botanical garden": (8, 1),
    "Polytechnic institute": (5, 4),
    "Market": (3, 5),
    "Shopping center": (1, 4),
    "Hospital": (3, 0),
    "Park": (6, 0),
    "Stadium": (8, 4),
    "Airport": (10, 2),
    "Library": (4, 3),
    "Residential area1": (1, 1),
    "Residential area2": (5, 4),
    "Residential area3": (4, 3),
    "Residential area4": (11, 12),
    "Residential area5": (12, 13),
}


paths = [
    ("Airport", "Train station", 5),
    ("Airport", "Center", 5),
    ("Train station", "Center", 7),
    ("Center", "Independence square", 7),
    ("Center", "University", 8),
    ("Independence square", "Botanical garden", 8),
    ("University", "Polytechnic institute", 3),
    ("Polytechnic institute", "Market", 3),
    ("Botanical garden", "Market", 11),
    ("Market", "Shopping center", 11),
    ("Market", "Park", 12),
    ("Shopping center", "Library", 12),
    ("Park", "Hospital", 6),
    ("Hospital", "Stadium", 6),
    ("Library", "Stadium", 8),
    ("Stadium", "Residential area1", 8),
    ("Residential area1", "Residential area2", 2),
    ("Residential area2", "Residential area3", 1),
    ("Botanical garden", "Residential area4", 11),
    ("Independence square", "Residential area5", 12),
]


def add_nodes(G, objects):
    for object in objects:
        G.add_node(object, pos=objects[object])


def add_path(G, paths):
    for path in paths:
        G.add_edge(path[0], path[1], weight=path[2])


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
