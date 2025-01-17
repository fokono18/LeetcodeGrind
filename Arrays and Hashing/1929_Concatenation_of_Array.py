## unlike haskell that we learnt in cs141 where list comprehension is linear time, in python concatenation of strings is constant time therefore to double a list the best way to do this would be 
## to concatenate the list twice  it runs at constant time 
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums
        