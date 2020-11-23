"""
BFS Algorithm
"""
from collections import deque


def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph


def bfs_visited(ugraph, start_node):
    """
    bfs_visited, return a list of visited nodes
    """
    queque = deque()
    stnode = start_node
    graph = copy_graph(ugraph)

    queque.append(stnode)
    visited = set()
    visited.add(stnode)

    while (queque):
        deq = queque.popleft()
        if deq in graph:
            for neighbor in graph[deq]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queque.append(neighbor)

    return visited


def cc_visited(ugraph):
    """
    cc_visited, return a list of sets, each are connected nodes
    """
    remaining = []
    graph = copy_graph(ugraph)
    for each in graph:
        remaining.append(each)

    cclist = []
    while len(remaining):
        cluster = bfs_visited(graph, remaining.pop())
        cclist.append(cluster)

        for each in cluster:
            if each in remaining:
                remaining.remove(each)

    return cclist


def largest_cc_size(ugraph):
    """
    largest_CC_size, return size of largest cc_visited set
    """
    maxn = 1
    graph = copy_graph(ugraph)
    cclist = cc_visited(graph)

    if cclist:
        for item in cclist:
            if len(item) > maxn:
                maxn = len(item)

    if not graph:
        return 0
    else:
        return maxn


def compute_resilience(ugraph, attack_order):
    """
    return: len(largest_cc), len(largest_cc after removal 1st node), len(largest_cc after removal 1st and 2nd node)...
    """
    graph = copy_graph(ugraph)
    cclen = []
    cclen.append(largest_cc_size(graph))

    attacklist = deque()
    for each in attack_order:
        attacklist.append(each)

    while (attacklist):
        node = attacklist.popleft()

        if node in graph:
            del graph[node]

        for each in graph:
            if node in graph[each]:
                graph[each].remove(node)

        cclen.append(largest_cc_size(graph))

    return cclen
