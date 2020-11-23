"""
Degree distributions for graphs.
"""

#Representing directed graphs
EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """
        Takes the number of nodes and returns a dictionary
        corresponding to a complete directed graph
        with the specified number of nodes.
    """
    directed_graph = {}

    if num_nodes < 0:
        return directed_graph

    for node in range(num_nodes):
        directed_graph[node] = set([x for x in range(num_nodes)])
        directed_graph[node].remove(node)  # to remove self looping

    return directed_graph


def compute_in_degrees(diagraph):
    """
        Takes a directed graph digraph
        and computes the in-degrees for the nodes.
    """
    degree_of_graph = {}

    for node in diagraph:
        degree_of_graph[node] = 0

    for key in diagraph:
        for to_node in diagraph[key]:
            degree_of_graph[to_node] += 1

    return degree_of_graph


def in_degree_distribution(diagraph):
    """
        Takes a directed graph digraph
        and computes the unnormalized distribution of the in-degrees.
    """
    in_dgr_distro = {}

    dgr_num = compute_in_degrees(diagraph)

    for node in dgr_num:
        in_dgr_distro[dgr_num[node]] = in_dgr_distro.get(dgr_num[node], 0) + 1

    return in_dgr_distro
