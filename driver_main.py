"""
Author- Sharat Gujamagadi
Date- 06.01.2021

Main driver code to find the shortest path and runtime user options
"""
import json
import sys
from software.graph import Graph
from software.tsp import TSP


def driver(graph, start_node):
    """
        driver code to find the shortest path and cost value to travel
    """
    if len(graph.nodes) > 1:
        tps = TSP(start_node)
        travel_edges, min_cost = tps.calculate_sort_path(graph.nodes, graph.edges)
        print('Shortest route cost value {} and path {}\n'.format(min_cost, travel_edges))
        tps.plot_graph()
    else:
        raise ValueError('No more than 1 node found')

def main():
    """
        main driver function
    """

    # read the input from json
    configfile = './input.json'
    with open(configfile) as read_buffer:
        config_file = json.loads(read_buffer.read())
        cities = config_file["cities"]
        start_node = config_file["start_node"]

    # update the graph
    graph = Graph(cities)

    # find shortest path and cost to the input
    driver(graph, start_node)

    while True:
        user_input = input('Select the options:\n A. Add Node\n D. Delete Node\n E. Exit\n >>> ')
        if user_input.lower() == 'a':
            # user input to add the new node to the graph
            new_node = input('Please enter the new node number >>> ')
            if new_node not in graph.nodes:
                new_edges = input('please enter {} edge weights eg: 10, 20, 0 >>> '.format(len(graph.nodes)+1))
                graph.add_node(new_node, new_edges)

                # finding new path after updating new node
                driver(graph, start_node)

            else:
                print('Entered node {} is already exist in graph'.format(new_node))

        elif user_input.lower() == 'd':
            # user input to delete the existing node
            del_node = input('Please enter the new node number >>> ')
            graph.delete_node(del_node)

            # finding new path after updating new node
            driver(graph, start_node)

        elif user_input.lower() == 'e':
            # exit the program
            sys.exit()

        else:
            print('Wrong option, please enter valid input\n')

if __name__ == '__main__':
   main()