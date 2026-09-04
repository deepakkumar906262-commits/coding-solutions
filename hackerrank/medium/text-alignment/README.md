# String Validators

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

In Python, a string of text can be aligned *left, right* and *center*.

__.ljust(width)__

This method returns a left aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.ljust(width,'-')
    HackerRank----------  

---    
__.center(width)__

This method returns a centered string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.center(width,'-')
    -----HackerRank-----

---
__.rjust(width)__

This method returns a right aligned string of length *width*.

	>>> width = 20
	>>> print 'HackerRank'.rjust(width,'-')
    ----------HackerRank
    
---
__Task__

You are given a partial code that is used for generating the _HackerRank Logo_ of variable _thickness_.  
Your task is to replace the blank (`______`) with *rjust, ljust* or *center*.




**Input Format**

 A single line containing the _thickness_ value for the logo.
 
 __Constraints__  

The *thickness* must be an *odd* number.  
$ 0 < thickness < 50$

**Output Format**

Output the desired logo.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T19:32:48.336Z  

```py
if __name__ == '__main__':
    
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/text-alignment/problem)