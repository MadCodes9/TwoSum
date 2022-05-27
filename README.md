# TwoSum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

## General Information 
This code is implemented by sorting the numbers first and creates a new array that excludes values in the sorted array
that is greater than the taget. The purpose of this is to shorten the array, so that in average cases the array will be 
smaller. Then, two pointers are used one at the first index of the array(i) and one at the last index of the array(j) and 
iterates depending on a few conditions. If the sum of the of the value at i and j are equilvalent to the traget then output
the index and finish, if i crosses j than increment i and reposition j at the end of the array, and if i is less than the 
length of the array then decrement j. 

****
```Python3
  while i < length:
       sum = shortarr[i] + shortarr[j]
       if sum == arg2:
          str2 = "Target {0} found at index [{1}, {2}]".format(arg2, i,j)
          print(str2)
          break
       if i >= j:
          i+=1
          j = len(shortarr) 
       j-=1
```


## Technologies
Project is created with 
* IDE: Microsoft Visual Studio 2019
* Version: 16.11.10
* Language: C++20
* 
## Setup
To run this project use Microsoft Visual Studio or an IDE that supports C++20 and download the .cpp and .h files into your IDE.
Asks user input to enter the size of the vector to be sorted with six different algorithms.

**Sample Output**

![Image](https://github.com/MadCodes9/Sorts/blob/main/500p1.png)
![Image](https://github.com/MadCodes9/Sorts/blob/main/500p2.png)

## Status 
This is a project created by @MadCodes9 :grinning:

Source: *Data Structures and Algorithms in C++ 2nd Edition*
