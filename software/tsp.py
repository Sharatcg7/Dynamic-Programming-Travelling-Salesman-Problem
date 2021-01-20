"""
Author - Sharat Gujamagadi
Date - 06.01.2021

Approach - Dynamic programing
resource - https://www.youtube.com/watch?v=XaXsJJh-Q5Y

Traveling sales man problem

"""
import copy
import time
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class TSP(object):
    def __init__(self, start_node=1):
        self.edges = None
        self.nodes = None
        self.start_node = start_node
        self.num_nodes = None
        self.p = []
        self.g = {}
        self.travel_edges = []

    def get_minimum(self, k, a):
        """
            returns the min cost among all the possible states
        """
        if (k, a) in self.g:
            return self.g[k, a]

        values = []
        all_min = []
        for j in a:
            set_a = copy.deepcopy(list(a))
            set_a.remove(j)
            all_min.append([j, tuple(set_a)])
            result = self.get_minimum(j, tuple(set_a))
            values.append(self.edges[self.nodes.index(str(k))][self.nodes.index(str(j))] + result)

        # get mini value from set as optimal solution
        self.g[k, a] = min(values)
        self.p.append(((k, a), all_min[values.index(self.g[k, a])]))

        return self.g[k, a]

    def calculate_sort_path(self, node, edges):
        """
            implementation of dynamic programming to find the shortest path
        """
        self.edges = edges
        self.nodes = node
        self.num_nodes = len(node)

        for x, y in enumerate(self.nodes):
            if x != self.nodes.index(str(self.start_node)):
                self.g[int(y), ()] = edges[x][0]

        next_node = self.nodes
        next_node = [int(i) for i in next_node]
        next_node.remove(self.start_node)

        # find min cost
        min_cost = self.get_minimum(self.start_node, tuple(next_node))

        # best path
        self.travel_edges.append(self.start_node)
        solution = self.p.pop()
        self.travel_edges.append(solution[1][0])
        for x in range(self.num_nodes - 2):
            for new_solution in self.p:
                if tuple(solution[1]) == new_solution[0]:
                    solution = new_solution
                    self.travel_edges.append(solution[1][0])
                    break
        self.travel_edges.append(self.start_node)

        return self.travel_edges, min_cost

    def plot_graph(self):
        """
            Graph plot along with highlighted shortest path

            reference - https://stackoverflow.com/questions/20133479/how-to-draw-directed-graphs-using-networkx-in-python
        """

        fig = plt.figure()
        edge_labels = {}
        node_labels = {}

        G = nx.from_numpy_matrix(np.array(self.edges), create_using=nx.DiGraph)
        pos = nx.shell_layout(G)

        for x, y, data in G.edges(data=True):
            edge_labels[(x, y)] = data['weight']
            node_labels[x] = self.nodes[x]

        # Graph
        nx.draw(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        nx.draw_networkx_labels(G, pos, labels=node_labels)

        # Image file formatter
        time_str = time.strftime('%Y-%m-%d-%H-%M')

        # Highlight the traveled path
        self.travel_edges = [self.nodes.index(str(edges)) for edges in self.travel_edges]
        highlighted_path_edges = list(zip(self.travel_edges, self.travel_edges[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=highlighted_path_edges, edge_color='r')
        fig.savefig("saved_graphs/TSP_Graph_" + str(time_str) + ".png")