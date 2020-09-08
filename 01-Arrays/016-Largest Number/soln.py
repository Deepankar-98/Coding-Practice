from functools import cmp_to_key

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A=list(map(str,A))
        cmpf=(lambda x,y: 1 if x+y>=y+x else -1)
        key=cmp_to_key(cmpf)
        A.sort(key=key,reverse=True)
        result="".join(A)
        result=result.lstrip('0')
        return result if result else '0'