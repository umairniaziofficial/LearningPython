import matplotlib.pyplot as plt
import networkx as nx

def ReturnPoints(Graph):
    G = nx.Graph(Graph)
    G.add_edges_from(Graph)
    return G

def DrawGraph(G):
    thelayout = nx.shell_layout(G)
    nx.draw(G,thelayout,with_labels=True,node_color="lightblue",edge_color="black")
    plt.show()


abc = [('A','B'),('B','C'),('C','D'),('D','A')]
ans = ReturnPoints(abc)
DrawGraph(ans)
print(ans)