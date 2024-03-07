# Eulerian Path - Create a program which will take as an input a graph and output either a Eulerian path or a Eulerian cycle, or state that it is not possible. A Eulerian Path starts at one node and traverses every edge of a graph through every node and finishes at another node. A Eulerian cycle is a eulerian Path that starts and finishes at the same node.

import networkx as nx

def is_eulerian(graph):
    if nx.is_eulerian(graph):
        if nx.has_eulerian_path(graph):
            return "Eulerian Path"
        else:
            return "Eulerian Cycle"
    else:
        return "Not possible"

# Example usage:
if __name__ == "__main__":
    g = nx.Graph()
    g.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

    result = is_eulerian(g)
    print(f"Eulerian Path/Cycle: {result}")

