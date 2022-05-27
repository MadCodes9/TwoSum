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
```C++
void Sorts::randomizedQuickSort(vector<int>& V) {
    if (V.size() <= 1)
        return;
    randomizedQuickSortStep(V, 0, V.size() - 1);

}
void Sorts::randomizedQuickSortStep(vector<int>& V, int a, int b) {
    if (a >= b)
        return;
    srand(time(NULL));
    int n = a + (rand() % (b - a)); //random number between a and b
    int pivot = V.at(n);    //to randomnize pivot 
    int tmp = V.at(b);  //pivot stays at same random position, but points to last element 
    V.at(b) = V.at(n);
    V.at(n) = tmp;

    int l;
    int r;
    l = a;
    r = b - 1;
    while (l <= r)
    {
        while (l <= r && (V.at(l) <= pivot))
            l++;
        while (r >= l && (V.at(r) >= pivot))
            r--;
        if (l < r)
        {
            int temp = V.at(r);
            V.at(r) = V.at(l);
            V.at(l) = temp;
        }
    }
    int temp = V.at(l);
    V.at(l) = V.at(b);
    V.at(b) = temp; // switch pivot to E
    randomizedQuickSortStep(V, a, l - 1);
    randomizedQuickSortStep(V, l + 1, b);

}
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
