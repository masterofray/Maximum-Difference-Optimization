# MAXIMUM Difference Optimization

## Problem
We are given **A**, a set of **N** integers $$[a_1, a_2, ... , a_n]$$ and each of integer $$a_i$$ ranges between $$A_{low}$$ and $$A_{high}$$. Make sure the difference between the maximum and minimum is equal or more than $$MAX_{DIFF}$$.
If we transform *A* into another array of integers *B*, the $$MAX_{DIFF}$$ does not exceed the range of $$B_{Hight}-B_{Low}$$. To do this we are free to add or substract each element of *A* by some integer, but the cost of operation proportional to $$\sum_{i=1}^{n} (b_i - a_i)^2$$.

### Sample Input
size of *A* and $$MAX_{DIFF}$$
A set of numbers $$A = [a_2, a_2, ... , a_n]$$
example input:
```
4 10
1
5
10
15
```

## Solution
* An array of integers $$B = [b_1, b_2, ... , b_n]$$ with $$B_{Max} - B_{Min} \leq MAX_{DIFF}$$ which minimize $$\sum_{i=1}^{n} b_i - a_i^2$$ to transfrom $$A$$ into $$B$$ 
* From the input we know that $$MAX_{DIFF} = 10$$ and $$A = \left[1, 5, 10, 15\right]$$.
* The optimum $$B$$ for minimizing the cost of $$A$$ is: $$B = \left[3, 5, 10, 13\right]$$.
* With the cost $$= (3 − 1)^2 + (5 − 5)^2 + (10 − 10)^2 + (15 − 13)^2 = 8$$.

### Output
The output is Cost to transform $$A$$ into $$B$$
example output:
```
8
```

## Contraint
We will design an algorithm to solve this problem given the input restriction:
1. First Contraint 
* $$1 < n < 1,000$$
* $$ 1 \leq A$$
* $$A_{Low} \leq a_i \leq A_{High} \leq 100$$
* $$MAX_{DIFF} \leq A_{high}-A_{low}$$

2. Second Constraint
* $$1 < n < 1,000$$
* $$ 1 \leq A$$
* $$A_{Low} \leq a_i \leq A_{High} \leq 10^{10}$$
* $$MAX_{DIFF} \leq A_{high}-A_{low}$$


###### Author @Masterofray
email me at masterofray@gmail.com