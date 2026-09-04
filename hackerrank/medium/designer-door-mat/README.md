# Text Wrap

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
**Submitted:** 2026-09-04T19:40:46.411Z  

```py


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/designer-door-mat/problem)