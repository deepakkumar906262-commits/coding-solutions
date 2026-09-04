# Designer Door Mat

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications: 

- Mat size must be $N  $X$  M$. ($N$ is an odd natural number, and $M$ is $3$ times $N$.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use `|`, `.` and `-` characters.

__Sample Designs__

```
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
```    



**Input Format**

A single line containing the space separated values of $N$ and $M$.  


**Constraints**

+ $5 < N < 101$
+ $15 < M < 303$

**Output Format**

Output the design pattern.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T19:41:47.424Z  

```py
# Read space-separated values of N and M
n, m = map(int, input().split())

# Top half of the door mat
for i in range(1, n, 2):
    print((".|." * i).center(m, '-'))

# Welcome line in the center
print("WELCOME".center(m, '-'))

# Bottom half of the door mat (reverse of the top half)
for i in range(n - 2, 0, -2):
    print((".|." * i).center(m, '-'))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/designer-door-mat/problem)