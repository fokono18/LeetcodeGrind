## The initial logic used was to compare the length of the set(nums) to the length of nums and if they differ then there exists duplicates otherwise there ar no duplicates
## but the time complexity of converting a list to a set is O(n) which is not bad but we can do better.
## Thats why instead i used this implementation it also has a time complexity of O(n) on average but best case scenario is O(1) whuch is much better than the other one that had a constant linear time
## this implementaion creates a set named list1 and checks if each element in nums is in list1, if it is in one that means there's a duplicate and we can just return true and break
## otherwise we keep going to the end of the list nums
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        list1 = set()

        for num in nums:
            if num in list1:
                return True
            list1.add(num)
        return False