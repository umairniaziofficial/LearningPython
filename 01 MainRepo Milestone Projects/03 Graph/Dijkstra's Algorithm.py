# Dijkstra's Algorithm - Create a program that finds the shortest path through a graph using its edges.

import networkx as nx

def dijkstra_algo(graph, start_node, end_node):
    shortest_path = nx.shortest_path(graph, source=start_node, target=end_node)
    shortest_distance = nx.shortest_path_length(graph, source=start_node, target=end_node)
    return shortest_path, shortest_distance

if __name__ == "__main__":
    g = nx.Graph()
    g.add_edges_from([(1, 2, {'weight': 1}), (2, 3, {'weight': 2}), (3, 4, {'weight': 3}), (4, 1, {'weight': 4})])

    start_node = 1
    end_node = 3

    result_path, result_distance = dijkstra_algo(g, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {result_path}")
    print(f"Shortest distance: {result_distance}")

