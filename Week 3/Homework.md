# Question 1
  Given a graph g, what set X does Algorithm Mystery compute?

### Answer:
    The set of all nodes that have degree 0

----
# Question 2
  Which of the following terms gives the tightest possible bound on the best-case running time of Algorithm Mystery?

### Answer:
    O(n)

----
# Question 3
  Which of the following terms gives the tightest possible bound on the worst-case running time of Algorithm Mystery?

### Answer:
    O(n^2)

----
# Question 4
  Which of the following choices is the tightest upper bound for the function f(n) = n(n+1)/2 ?
### Answer:
    f(n) is O(n^2)

----
# Question 5
  Which of the following choices is the tightest upper bound for the function f(n) = 1/(2^n) ?

### Answer:
    f(n) is O(1)

----
# Question 6
  Which of the following choices is the tightest upper bound for the function f(n) = (n^2)/(1+n) ?

### Answer:
    f(n) is O(n)

----
# Question 7
  Which of the following choices is the tightest upper bound for the function f(n) = n^3 - n^2

### Answer:
    f(n) is O(n^3)

----
# Question 8
  Let f(n) = a0 + a1 n + a2 n^2 + a3 n^3. In proving that f(n) is O(n^3), what is the smallest value for the constant c consistent with n_0 = 1? (You should assume that the a_i are positive.)

### Answer:
    a0+a1+a2+a3

----
# Question 9
  Let f(n) = a0 + a1 n + a2 n^2 + a3 n^3. In proving that f(n) is O(n^3), what is the smallest value for the constant c consistent with n_0 = 2? (You should assume that the a_i are positive.)

### Answer:
    a0/8 + a1/4 + a2/2 + a3

----
# Question 10
  In proving that 3n + 5 is Θ(n), what are the two associated constants for the lower and upper bounding functions (largest possible value for the lower bound, smallest possible value for upper bound), assuming that we wish to prove this bound for n_0 = 1?

### Answer:
    3 8

----
# Question 11
  The skeleton is missing information on Lines 5, 8, 10, and 11 in the CC Distance Algorithm. Which of the following options completes the pseudo-code so that it correctly computes the set of all CCs of a graph?

### Answer:
    Line 5 : g,i
    Line 8 : d_u != infinity
    Line 10 : CC U {W}
    Line 11 : RemainingNodes - W

----
# Question 12
  If a graph g is given by its adjacency list, has n nodes and m edges, which of the following expressions gives the tightest upper bound on the worst-case running time of CC-Distance (as given by the pseudo-code in the previous question) on the graph g?

  You may assume that the running times of the set operations in CC-Distance are proportional to the number of elements being added to or removed from the set.

### Answer:
    O(n^2)

----
# Question 13
  The skeleton of Algorithm CC-Visited is missing information on Lines 5, 6, and 7. Which of the following options completes the pseudo-code so that it correctly computes the set of all CCs of a graph?

### Answer:
    Line 5 : g,i
    Line 6 : CC U {W}
    Line 7 : RemainingNodes - W

----
# Question 14
  If a graph g is given by its adjacency list, has n nodes and m edges, which of the following terms gives the tightest upper bound on the worst-case running time of CC-Visited (as given by the pseudo-code in the previous question) on the graph g?
  
  You may assume that the running times of the set operations in BFS-Visited and CC-Visited are proportional to the number of elements being added to or removed from the set.

### Answer:
    O(m+n)

----
# Question 15
  Which of the following statements is true concerning the running times for Algorithm CC-Distance and Algorithm CC-Visited?

### Answer:
    The running time of CC-Distance is asymptotically slower than that of CC-Visited due to the initialization of d in lines 2-3 of BFS Distance.

----
# Question 16
  If A is the adjacency matrix for a graph g, what is the number of paths of length k from node i to node j in g? Note that this answer should include simple paths (no cycles allowed) and non-simple paths (cycles allowed).

### Answer:
    (A^k)[i,j]

----
# Question 17
  If A is the adjacency matrix for a graph g, what is the length of the shortest path from node i to node j in g?

### Answer:
    The length of the shortest path is the smallest non-negative integer k such that (A^k)[i,j] is non-zero.

----
# Question 18
  If A is the adjacency matrix for g and A_hat is the adjacency matrix for the graph g_hat created by removing e (but not its endpoints) from g, which of the following expressions corresponds to the number of shortest paths from node i to node j that include the edge e? You may assume that there exists at least one path from node i to node j in g.

### Answer:
    (A^k)[i,j] - (A_hat^k)[i,j] where k is the length of the shortest path from node i to node j in g.

----
