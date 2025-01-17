from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ## initiate a max of -1
        ## compare the new max to the old max
        ## if the max is bigger swap that
        ## return the array
        InitialMax = -1
        for i in range(len(arr)-1, -1, -1):
            NewMax = max(InitialMax, arr[i])
            arr[i] = InitialMax
            InitialMax = NewMax
        return arr
        