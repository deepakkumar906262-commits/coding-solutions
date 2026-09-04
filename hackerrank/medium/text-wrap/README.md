# Text Alignment

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

<sub>Check [Tutorial](https://www.hackerrank.com/challenges/text-wrap/tutorial) tab to know how to to solve.</sub>  

You are given a string $S$ and width $w$.  
Your task is to wrap the string into a paragraph of width $w$.  

**Function Description**   

Complete the *wrap* function in the editor below.  

*wrap* has the following parameters:   

- *string string:* a long string   
- *int max_width:* the width to wrap to   

**Returns**   

- *string:* a single string with newline characters ('\n') where the breaks should be   

**Input Format**

The first line contains a string, $string$.  
The second line contains the width, $max_width$.



**Constraints**

+ $0 < len(string) < 1000$  
+ $0 < max_width < len(string)$



**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-09-04T19:39:17.388Z  

```py
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/text-wrap/problem)