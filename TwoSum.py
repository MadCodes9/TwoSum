import itertools
from typing import List


def twoSum(arg1: List[int], arg2):
   # TODO: Sort the numbers before function call to iterate values quicker
   sort = sorted(arg1)
   print(list(sort))

   # TODO: Use takewhile to return a shorten array of values that are less 
   # than the target 
   shortarr = list(itertools.takewhile(lambda x: x < arg2, sort))
   print(shortarr) 

   #TODO: Find two values in the shorten array that are equal to the target
   i = 0
   j = len(shortarr) - 1
   length = len(shortarr)
   
   while i < length:
       sum = shortarr[i] + shortarr[j]
       if sum == arg2:
          str1 = "[{0}, {1}]".format(i,j)
          print(str1)
          break
       if i >= j:
          i+=1
          j = len(shortarr) 
       j-=1

def main():
    nums = [3, 5, 10, 1, 6]
    target = 9
    twoSum(nums, target)

if __name__ == "__main__":
    main()