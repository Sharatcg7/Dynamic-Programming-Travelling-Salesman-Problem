"""
Author - Sharat Gujamagadi
Date - 06.01.2021

source- https://www.tutorialspoint.com/python_data_structure/python_graphs.htm
graph class to add, delete the nodes and edges

Future implementation- Update existing node's edge weights

"""

class Graph(object):
    def __init__(self, gragh=None):
        if gragh is None:
            gragh = []
        self.g_dict = gragh
        self.nodes = list(self.g_dict.keys())
        self.edges = list(self.g_dict.values())

    def get_nodes(self):
        """
           returns the nodes
        """
        return self.g_dict.keys()

    def get_edges(self):
        """
            returns the edges which are connected between two nodes
        """
        return self.g_dict.values()

    def add_node(self, new_node, new_edge):
        """
            Adding the new node to the graph and add the edge weight
        """
        new_edge = new_edge.split(', ')
        if len(new_edge) == len(self.nodes) + 1:
            new_edge = [int(i) for i in new_edge]
            self.g_dict[new_node] = new_edge
            self.nodes.append(new_node)
            self.edges.append(new_edge)

            # Adding edge weights
            for i, j in enumerate(self.g_dict):
                if not i+1 == len(self.nodes):
                    self.g_dict[str(i+1)].append(new_edge[i])
        else:
            raise IndexError("Please enter {} number of edge values".format(len(self.nodes)+1))


    def delete_node(self, del_node):
        """
            Removing the node from the graph, raise an error if node does not exist
        """
        if del_node in self.nodes:
            del_index = self.nodes.index(del_node)
            del self.nodes[del_index]
            del self.edges[del_index]
            del self.g_dict[del_node]

            for key in self.g_dict.keys():
                del self.g_dict[key][del_index]

            print("updated graph parameter {}".format(self.g_dict))

        else:
            raise ValueError('Entered {} node is not present in graph to delete'.format(del_node))