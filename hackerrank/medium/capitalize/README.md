# Alphabet Rangoli

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, `alison heck` should be capitalised correctly as `Alison Heck`. 

$\color{red}\texttt{a}\color{black}\texttt{lison}\ \color{red}\texttt{h}\color{black}\texttt{eck}\ \color{black} \Rightarrow \color{black}\texttt{Alison}\ \color{black}\texttt{Heck}$

Given a full name, your task is to _capitalize_ the name appropriately.

**Input Format**

A single line of input containing the full name, $S$.

**Constraints**

+ $0 < len(S) < 1000$  
+ The string consists of alphanumeric characters and spaces.  

**Note:** in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc. 

**Output Format**

Print the capitalized string, $S$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T19:47:44.019Z  

```py
def print_rangoli(size):
    import string
    # Get all lowercase letters
    alpha = string.ascii_lowercase
    
    lines = []
    for i in range(size):
        # Slice letters starting from the outermost character moving inward
        s = "-".join(alpha[size - 1 : i : -1] + alpha[i : size])
        # Center the string using hyphens to fill the total width
        lines.append(s.center(4 * size - 3, "-"))
        
    # Combine the top half, center line, and bottom half symmetrically
    print("\n".join(lines[::-1] + lines[1:]))


```

---

[View on HackerRank](https://www.hackerrank.com/challenges/capitalize/problem)