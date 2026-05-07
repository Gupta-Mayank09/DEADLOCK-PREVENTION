import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(allocation, request):
    G = nx.DiGraph()

    # Add nodes
    for p in allocation:
        G.add_node(p)
    for r in ["R1", "R2"]:
        G.add_node(r)

    # Allocation edges (Resource → Process)
    for p in allocation:
        for r in allocation[p]:
            G.add_edge(r, p)

    # Request edges (Process → Resource)
    for p in request:
        for r in request[p]:
            G.add_edge(p, r)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, font_size=10)
    plt.title("Resource Allocation Graph")
    plt.show()