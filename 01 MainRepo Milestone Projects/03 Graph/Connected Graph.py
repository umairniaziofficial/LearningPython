# Connected Graph - Create a program which takes a graph as an input and outputs whether every node is connected or not.

import networkx as nx

def is_connected(graph):
    return nx.is_connected(graph)

if __name__ == "__main__":
    g = nx.Graph()
    g.add_edges_from([(1, 2), (2, 3), (3, 1)])

    result = is_connected(g)
    print(f"Is the graph connected?: {'Yes, it is connected' if result else 'No, it is not connected'}")