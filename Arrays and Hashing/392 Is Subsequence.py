## subsequence problems involve dynamic programming the bes approach is to use pointers and go through both lists and check if element in s can be found in 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        if i == len(s):
            return True
        return False

