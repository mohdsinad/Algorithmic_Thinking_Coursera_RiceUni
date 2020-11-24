"""
Project 3: Closest Pairs and Clustering Algorithms
"""
import math
import alg_cluster

######################### Code for closest pairs of clusters #########################


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list
    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    Output: tuple (dist, idx1, idx2) where dist is distance between cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)
    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    if len(cluster_list) <= 1:
        return (0, 0, 0)
    minimum_distance = float('inf')
    idx1, idx2 = -1, -1
    for cluster_index, cluster in enumerate(cluster_list):
        for other_cluster_index, other_cluster in enumerate(cluster_list[cluster_index+1:], cluster_index+1):
            if cluster_index != other_cluster_index:
                current_distance = cluster.distance(other_cluster)
                if current_distance < minimum_distance:
                    minimum_distance = current_distance
                    idx1, idx2 = cluster_index, other_cluster_index
    return (minimum_distance, idx1, idx2)


def get_min_tuple(tuple_a, tuple_b):
    '''
    return the tuple with smalles first entry
    '''
    temporary_list = [tuple_a, tuple_b]
    temporary_list.sort(key=lambda x: x[0])
    return temporary_list[0]


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list
    Input: cluster_list is list of clusters SORTED such that horizontal positions of their centers are in ascending order
    Output: tuple of the form (dist, idx1, idx2) where the centers of cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    cluster_count = len(cluster_list)
    if cluster_count <= 3:
        return slow_closest_pair(cluster_list)
    else:
        mid_position = int(cluster_count // 2)
        left_list = cluster_list[: mid_position]
        right_list = cluster_list[mid_position:]
        mid = 0.5 * (left_list[-1].horiz_center() +
                     right_list[0].horiz_center())
        left_tuple = fast_closest_pair(left_list)
        right_dist, right_id1, right_id2 = fast_closest_pair(right_list)
        right_tuple = (right_dist, right_id1 + mid_position,
                       right_id2 + mid_position)
        min_tuple = get_min_tuple(left_tuple, right_tuple)
        strip_tuple = closest_pair_strip(cluster_list, mid, min_tuple[0])
        min_tuple = get_min_tuple(min_tuple, strip_tuple)
    return min_tuple


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    Input: cluster_list is a list of clusters produced by fast_closest_pair
           horiz_center is the horizontal position of the strip's vertical center line
           half_width is the half the width of the strip (i.e; the maximum horizontal distance that a cluster can lie from the center line)
    Output: tuple of the form (dist, idx1, idx2) where the centers of cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    defalut_tuple = (float('inf'), -1, -1)
    in_strip_pair = [(index, cluster) for index, cluster in enumerate(cluster_list)
                     if abs(cluster.horiz_center() - horiz_center) < half_width]

    in_strip_pair.sort(key=lambda pair: pair[1].vert_center())
    if len(in_strip_pair) <= 1:
        return defalut_tuple

    in_strip_index, in_strip = zip(*in_strip_pair)
    for cluster_index, cluster in enumerate(in_strip[:-1]):
        other_loop = in_strip[cluster_index+1: cluster_index+4]
        for other_cluster_index, other_cluster in enumerate(other_loop, cluster_index+1):
            current_distance = cluster.distance(other_cluster)
            if current_distance < defalut_tuple[0]:
                defalut_tuple = (current_distance,
                                 cluster_index, other_cluster_index)

    id_original = (in_strip_index[defalut_tuple[1]],
                   in_strip_index[defalut_tuple[2]])
    defalut_tuple = (defalut_tuple[0], min(id_original), max(id_original))
    return defalut_tuple

######################### Code for hierarchical clustering ###########################


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters. Note that the function may mutate cluster_list
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    cluster_list_copy = [clu.copy() for clu in cluster_list]
    cluster_count = len(cluster_list)
    while cluster_count > num_clusters:
        cluster_list_copy.sort(key=lambda clu: clu.horiz_center())
        _, id1, id2 = fast_closest_pair(cluster_list_copy)
        cluster_list_copy[id1].merge_clusters(cluster_list_copy.pop(id2))
        cluster_count -= 1

    return cluster_list_copy

######################### Code for k-means clustering ################################


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters. Note that the function may not mutate cluster_list
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """
    # position initial clusters at the location of clusters with largest populations
    cluster_list_copy, id_population_pair = zip(*[(clu.copy(), (index, clu.total_population()))
                                                  for index, clu in enumerate(cluster_list)])
    id_population_pair = list(id_population_pair)
    id_population_pair.sort(key=lambda x: -x[1])
    initial_cluster = [cluster_list_copy[id_population_pair[pair_id][0]]
                       for pair_id in xrange(num_clusters)]

    for dummy_iter in xrange(num_iterations):
        initial_cluster = [alg_cluster.Cluster(set([]), clu.horiz_center(
        ), clu.vert_center(), 0, 0) for clu in initial_cluster]

        holder_cluster = [clu.copy() for clu in initial_cluster]
        for cluster in cluster_list_copy:
            initial_cluster_dist_id = [(index, cluster.distance(
                clu)) for index, clu in enumerate(initial_cluster)]
            initial_cluster_dist_id.sort(key=lambda x: x[1])
            min_id = initial_cluster_dist_id[0][0]
            holder_cluster[min_id].merge_clusters(cluster)

        initial_cluster = holder_cluster
    return initial_cluster
