# Question 1
  Let X=AC and Y=CA be two DNA sequences. Which of the following are global alignments of X and Y?

### Answer:
    X′=AC and Y′=CA
    X′=AC−− and Y′=−−CA

----
# Question 2
  How many possible global alignments are there for two sequences X and Y if |X|=|Y|=1? How many possible global alignments are there for two sequences X and Y if |X|=|Y|=2?

### Answer:
    3 13

----
# Question 3
  Feasibility conditions of a sequence alignment that for X′ and Y′
  to be an alignment of two sequences X and Y, X′ and Y′ must satisfy the following condition (among other conditions):
  
  * There does not exist an i such that X'_i = Y'_i = -.
  
  What happens if we remove this condition; that is, allow X'_i = Y'_i = - for some values of i?

### Answer:
    The number if possible alignmnets of a pair of sequences becomes infinite.

----
# Question 4
  Consider the scoring matrix M for alphabet Σ={A,C,T,G} with the following entries:
  
  * M_σ,σ =5 for every σ ∈ Σ.
  * M_σ,σ′=2 for every σ,σ′∈Σ and σ != σ′.
  * M_σ,− =−2 for every σ∈Σ.
  * M_−,1σ=−4 for every σ∈Σ.

  What is the score of the following alignment:
  
  X'=AC--CT             
  Y'=TACGGT

### Answer:
    3

----
# Question 5
  Let X=AC and Y=GG be two DNA sequences (Σ={A,C,T,G}), and consider the scoring matrix MM given by:

  * M_σ,σ = 6 for every σ ∈ Σ.
  * M_σ,σ′= 2 for every σ,σ′∈Σ and σ != σ′.
  * M_σ,− = M_−,σ = −4 for every σ ∈ Σ.

  Under this scoring matrix, which pair of sequences below is the optimal global alignment of X and Y?

### Answer:
    X'= AC and Y'= GG.

----
# Question 6
  Let B(m,n) denote the number of global alignments of two sequences X and Y of lengths m and n, respectively. A recursive formula for B(m,n) is:

### Answer:
    B(m,n) = B(m-1,n) + B(m-1,n-1) + B(m,n-1).

----
# Question 7
  From the given GlobalAlignment Algorithm, We can notice that the entries S[i, j] of the global alignment matrix are the maximum scores for all possible global alignments for the pair of sequences X[0…i−1] and Y[0…j−1], which values of S will this dynamic programming method use in computing S[i, j] when i>0 and j>0?

### Answer:
    S[i-1,j-1], S[i-1,j], and S[i,j-1].

----
# Question 8
  Refer Picture

----
# Question 9
  The pseudo-code of the ComputeAlignment algorithm is missing details on Lines 1-6. Which of the following options completes the algorithm so that it correctly computes an optimal global alignment using the global alignment matrix S that was computed using Algorithm ComputeGlobalAlignmentScores?

### Answer:
    Line 1 : X_i-1 + X'
    Line 2 : Y_j-1 + Y'
    Line 3 : X_i-1 + X'
    Line 4 : "-" + Y'
    Line 5 : "-" + X'
    Line 6 : Y_j-1 + Y'

----
# Question 10
  Given two strings X and Y of lengths m and n, respectively, which of the following gives the tightest worst-case running time of Algorithm GlobalAlignment as given by the pseudo-code in Q7?

### Answer:
    O(mn)

----
# Question 11
  Given a string x of length n, how many substrings v of x are there?

### Answer:
    (n+2)!/(2*n!) - n

----
# Question 12
  2 strings X=AA and Y=TAAT over the alphabet Σ={A,C,T,G} and the scoring matrix MM given by:

  * M_σ,σ=10 for every σ ∈ Σ.
  * M_σ,σ′=4 for every σ,σ′∈Σ and σ !=σ′.
  * M_σ,− = M_−,σ = −6 for every σ ∈ Σ.
  
  Given the two sequences X and Y and the scoring matrix M, what values would the modified algorithm assign to the entries S[0,2], S[2,0] and S[2,2] of the local alignment matrix S?

### Answer:
    0 0 14

----
# Question 13
  what is the maximum value in an entry in the local alignment matrix S that you computed in Q12?

### Answer:
    20

----
# Question 14
  At what entry does the modified ComputeAlignment (in Q13) start the traceback and at what entry does it end the traceback?

### Answer:
    2 3 0 1

----
# Question 15
  Using the modified ComputeGlobalAlignmentScores and ComputeAlignment algorithms in Q12 and Q13, what is the local alignment they compute on the sequences X and Y using the scoring matrix in Q12?

### Answer:
    X' = AA and Y' = AA

----
# Question 16
  Given two strings X and Y of lengths m and n, respectively, which of the following gives the tightest worst-case running time of computing a local alignment of the two strings using the modified algorithms in Q12 and Q13?

### Answer:
    O(mn)

----
# Question 17
  If all entries in a scoring matrix MM are non-negative, then the score of an optimal local alignment and an optimal global alignment of two sequences X and Y using MM are identical. Is the above statement true or false?

### Answer:
    True
