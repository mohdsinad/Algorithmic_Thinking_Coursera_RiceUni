# Question 1
  How many inversions are there in the array A = [5, 4, 3, 6, 7]?

### Answer:
    3

----
# Question 2
  In an array with nn elements, what is the maximum possible number of inversions?

### Answer:
    n*(n-1)/2

----
# Question 3
  What is the best case running time of a brute-force algorithm that counts the number of inversions in an array with nn elements by checking every pair of elements in the array?

### Answer:
    O(n^2)

----
# Question 4
  Lines 1 and 2 in the function Merge are incomplete. Which of the following options completes these two lines so that the algorithm is correct?

### Answer:
    Line 1 : B|i| ≤ C|j|
    Line 2 : p - i

----
# Question 5
  Which of the following gives the recurrence that results in the tightest running time for Algorithm CountInversions?

### Answer:
    T(n) = 2T(n/2) + O(n)

----
# Question 6
  Which of the following gives the tightest order of growth for the solution of the following recurrence?
  
  * T(n) = 4T(n/2)+n
  * T(1) = 1

### Answer:
    O(n^2)

----
# Question 7
  Which of the following gives the tightest order of growth for the solution of the following recurrence?
  
  * T(n) = 4T(n/2)+n^3 
  * T(1) = 1

### Answer:
    O(n^3)

----
# Question 8
  What does Mystery([-2,0,1,3,7,12,15],0,6) compute?

### Answer:
    3

----
# Question 9
  What does Algorithm Mystery compute when run on input (A[0..n-1],0,n-1)?

### Answer:
    Returns i if there exists an i such that A[i] = i and -1 otherwise

----
# Question 10
  What are the best case and worst case running times of Algorithm Mystery as a function of the input size n (and assume l≤r in the input)?

### Answer:
    Best case : O(1)
    Worst case: O(log n)

----
# Question 11
  Let S(n,k) denote the number of ways that a set of n points can be clustered into k non-empty clusters. Which of the following is a correct recurrence for S(n,k), for n≥1? Assume, for the base cases, that S(n, n) = S(n, 1) = 1.

### Answer:
    S(n,k) = k S(n-1,k) + S(n-1,k-1)

----
# Question 12
  Which of the following formulas gives the number of ways of clustering a set of nn points into 2 non-empty clusters; that is, a solution to the recurrence from the previous question for k=2?

### Answer:
    2^(n-1) - 1

----
# Question 13
  Assuming that Line 4 of the HierarchicalClustering takes h(n) time in each iteration, for some function h, which of the following gives the tightest worst-case running time of the algorithm as a function of the number of points, n, when k is one? Assume that the union and difference of two sets A and B takes O(|A|+|B|) time to compute.

### Answer:
    O(n^2 + h(n)n)

----
# Question 14
  Which of the following gives the tightest worst-case running time of the KMeansClustering algorithm as a function of the number of points, n, and the number of clusters k, and the number of iterations q? Assume that adding {p_j} to C_l in line 7 takes O(1) time.

### Answer:
    O(q k n)

----
# Question 15
  Consider a list of nn numbers sorted in ascending order. Which of the following gives the worst-case running time of the most efficient algorithm for finding a closest pair of numbers in this list?

### Answer:
    O(n)

----
# Question 16
  Which of the following gives the tightest worst-case running time of the SlowClosestPair algorithm in terms of the number of points n?

### Answer:
    O(n^2)

----
# Question 17
  If the helper function ClosestPairStrip used in the conquer step in line 11 has a worst case running time that is O(f(n)), which of the following recurrences models the running time of FastClosestPair? You may assume that ClosestPairStrip examines all of its input and, therefore, f(n) grows at least as fast as n. (Here, d is a constant.)

### Answer:
    T(n) = 2T(n/2) + f(n)
    T(2) = d

----
# Question 18
  If n is the size of the input P, what is the worst case running time of ClosestPairStrip?

### Answer:
  O(nlog(n))

----
# Question 19
  Based on your answers to Q17 and Q18, what is the worst case running time of FastClosestPair?

### Answer:
  O(n log^2(n))

----
# Question 20
  If the algorithm for ClosestPairStrip could be modified such that its running time f(n) is O(n), what would be the worst case running time of FastClosestPair?

### Answer:
  O(nlog(n))

----
