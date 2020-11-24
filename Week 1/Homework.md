# Question 1
  What is the degree of node 7 in the given undirected graph?

### Answer:
    0

----
# Question 2
  If A is the adjacency matrix representation for the undirected graph in Q1, what is the value of A[2,6]?

### Answer:
    1

----
# Question 3
  Which one of the following is a (Python) dictionary representation of the degree distribution of the graph in Q1?

### Answer:
    {0: 0.125, 1: 0.125, 2: 0.25, 3: 0.375, 4: 0.125}

----
# Question 4
  How many nodes in the graph have in-degree 2 in the given directed graph?
  
### Answer:
    5

----
# Question 5
  If A is the adjacency matrix of the graph in Q4, what is the value of entry A[2,1]?

### Answer:
    0

----
# Question 6
  How many nodes in the graph of Question 4 have out-degree 2?

### Answer:
    4

----
# Question 7
  Consider an undirected graph g=(V,E) where |V|=n. What is the maximum possible degree of a node in g?

### Answer:
    n-1

----
# Question 8
  Consider an undirected graph g=(V,E) where |V|=n. What is the maximum possible number of edges in g? That is, what is the largest size that E can be?

### Answer:
    n*(n-1)/2

----
# Question 9
  In an undirected graph g=(V,E) with n nodes, in how many ways can we connect a specific node uu to other nodes in g so that u has degree k (where 0 ≤ k < n )?

### Answer:
    ( n-1 )
    (  k  )
----
# Question 10
  Suppose that the graph g produced by running the given Algorithm ER(n,p). What are lower and upper bounds on the degrees for nodes in g?

### Answer:
    Lower bound = 0 & Upper bound = n-1

----
# Question 11
  How many edges are there in a graph g that is obtained by running the given Algorithm ER(10,0)? 

### Answer:
    0

----
# Question 12
  How many edges are there in a graph g that is obtained by running the given Algorithm ER(10,1)? 

### Answer:
    45

----
# Question 13
  What is the expected value of the degree of a node in a graph g that is obtained by running the given Algorithm ER(n,p)?

### Answer:
    (n-1)p

----
# Question 14
  What is the probability that a particular node in a graph g produced by running the given Algorithm ER(n,p) has degree k where 0 ≤ k < n?

### Answer:
    (n-1) p^k (1-p)^(n-1-k)
    ( k )

----
# Question 15
  Consider a graph g that is obtained by running the given Algorithm ER(n,p). If g is represented by its adjacency matrix, which of the following expressions in n and p grows at the same rate as the running time of ER(n,p)?

### Answer:
    n^2

----
# Question 16
  Consider a graph g that is obtained by running the given Algorithm ER(n,p) where p=0. If g is represented by its adjacency matrix, which of the following expressions in n and p grows at the same rate as the running time of ER(n,p)?

### Answer:
    n^2

----
# Question 17
  Let g be an undirected graph that has n nodes and m edges. If g is given by its adjacency matrix, which of the following expressions grows at the same rate as the time that it takes to compute the degree distribution of g?

### Answer:
    n^2

----
# Question 18
  Let g be an undirected graph that has n nodes and m edges. If g is given by its adjacency list, which of the following expressions grows at the same rate as the time that it takes to compute the degree distribution of g?

### Answer:
    m + n

----
