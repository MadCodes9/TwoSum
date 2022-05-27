import itertools
from typing import List


def twoSum(arg1: List[int], arg2):
   # TODO: Sort the numbers before function call to iterate values quicker
   sort = sorted(arg1)

   # TODO: Use takewhile to return a shorten array of values that are less 
   # than the target 
   shortarr = list(itertools.takewhile(lambda x: x < arg2, sort))
   str1 = "Shorten Array: {0}".format(shortarr)
   print(str1) 

   #TODO: Find two values in the shorten array that are equal to the target
   i = 0
   j = len(shortarr) - 1
   length = len(shortarr)
   
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

def main():
    nums = [3, 5, 10, 1, 6]
    target = 9
    str = "Original Array: {0}".format(list(nums))
    print(str)
    twoSum(nums, target)

if __name__ == "__main__":
    main()