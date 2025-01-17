## This is lowkey the fastest way i think to do it i initially assigned the counter(s) to a variable and did the same for t and compared their their values
## This has a time complexity of O(n)
from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)